from openai.types import embedding
import pandas as pd
import openai
import numpy as np
from dotenv import dotenv_values
from tenacity import retry, wait_random_exponential, stop_after_attempt
import pickle

cache_path = "data/career_cache.pkl"
try:
    embedding_cache = pd.read_pickle(cache_path)
except FileNotFoundError:
    embedding_cache = {}
with open(cache_path, "wb") as cache_file:
    pickle.dump(embedding_cache, cache_file)

# ① ファイル読み込み関数
# 　→ openとsplitだけ使えば書ける
def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# ② Embedding関数
# 　→ 12章で既にやった。見ないで書けるはず
@retry(wait=wait_random_exponential(min=1, max=20), stop=stop_after_attempt(6))
def get_embedding(text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")
    max_chars = 32000
    if len(text) > max_chars:
        text = text[:max_chars]
    return openai.embeddings.create(input=[text], model=model).data[0].embedding

def embedding_from_string(string, model="text-embedding-3-small", embedding_cache=embedding_cache):
    if (string, model) not in embedding_cache.keys():
        embedding_cache[(string, model)] = get_embedding(string, model)
        with open(cache_path, "wb") as cache_file:
            pickle.dump(embedding_cache, cache_file)
    return embedding_cache[(string, model)]

# ③ コサイン類似度関数
# 　→ np.dotとnp.linalg.normを使う
def indices_of_nearest_neighbors(query_embedding, embeddings):
    similarities = [
        np.dot(query_embedding, embedding) / (np.linalg.norm(query_embedding) * np.linalg.norm(embedding))
        for embedding in embeddings
    ]
    return np.argsort(similarities)[::-1]  


# ④ 類似段落検索関数
# 　→ ③を使ってループを書く
def recommendations_from_strings(string, paragraphs, embeddings, model="text-embedding-3-small", k_nearest_neighbors=1,):
    query_embedding = get_embedding(string, model)
    nearest_indices = indices_of_nearest_neighbors(query_embedding, embeddings)

    results = []
    for i in nearest_indices:
        if string == paragraphs[i]:
            continue
        if len(results) >= k_nearest_neighbors:
            break
        results.append(paragraphs[i])
        
    return results

# ⑤ GPTに回答させる関数
# 　→ 6章のチャットボットと同じ構造
def answer_question(query, context_paragraphs): 
    context_paragraphs = "\r\n\r\n".join(context_paragraphs)
    messages = [
        {
            "role": "system",
            "content": f"""あなたはキャリア相談AIです。以下のコンテキストをもとに質問に日本語で答えてください。コンテキストに含まれない情報は「情報がありません」と答えてください。

            コンテキスト:
                {context_paragraphs}
            """},
        {"role": "user", "content": query}
    ]
    response = openai.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )
    return response.choices[0].message.content

def main():
    paragraphs = [p.strip() for p in read_file("data/career_data.txt").split("\r\n\r\n") if p.strip()]
    embeddings = [embedding_from_string(paragraph) for paragraph in paragraphs]

    while True:
        query = input("Enter your question: ")
        if query.lower() == "exit":
            break
        context_paragraphs = recommendations_from_strings(query, paragraphs, embeddings)
        answer = answer_question(query, context_paragraphs)
        print(answer)

if __name__ == "__main__":
    config = dotenv_values(".env")
    openai.api_key = config["OPENAI_API_KEY"]

    main()