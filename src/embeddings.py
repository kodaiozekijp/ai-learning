import openai
import pandas as pd
import numpy as np
import pickle
from dotenv import dotenv_values
from tenacity import retry, wait_random_exponential, stop_after_attempt
from nomic import atlas

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

dataset_path = "data/wiki_movie_plots_deduped.csv"
df = pd.read_csv(dataset_path)
movies = df[df["Origin/Ethnicity"] == "Japanese"].sort_values("Release Year", ascending=False).head(1000)
movie_plot = movies["Plot"].values

@retry(wait=wait_random_exponential(min=1, max=20), stop=stop_after_attempt(6))
def get_embedding(text, model="text-embedding-3-small"):

    # replace newlines, which can negatively affect performance.
    text = text.replace("\n", " ")

    # Truncate text to fit within the 8192 token limit
    # 1 token ≈ 4 characters, so the character limit is 8192 × 4 = 32768
    max_chars = 32000  # Add a little extra space
    if len(text) > max_chars:
        text = text[:max_chars]

    return  openai.embeddings.create(input=[text], model=model).data[0].embedding

# establish a cache of embeddings to avoid recomputing
# cache is a dict of tuples (text, model) -> embedding, saved as a pickle file

# set path to embedding cache
embedding_cache_path = "data/movie_embeddings.pkl"

# load the cache if it exists, and save a copy to disk
try:
    embedding_cache = pd.read_pickle(embedding_cache_path)
except FileNotFoundError:
    embedding_cache = {}
with open(embedding_cache_path, "wb") as embedding_cache_file:
    pickle.dump(embedding_cache, embedding_cache_file)

# define a function to retrieve embeddings from the cache if present, and otherwise request via the API
def embedding_from_string(string, model="text-embedding-3-small", embedding_cache=embedding_cache):
    if (string, model) not in embedding_cache.keys():
        embedding_cache[(string, model)] = get_embedding(string, model)
        print(f"GOT EMBEDDING FOR {string[:20]}")
        with open(embedding_cache_path, "wb") as embedding_cache_file:
            pickle.dump(embedding_cache, embedding_cache_file)
    return embedding_cache[(string, model)]

plot_embeddings = [embedding_from_string(plot, model="text-embedding-3-small") for plot in movie_plot]
data = movies[["Title", "Genre"]].to_dict("records")

atlas_project = atlas.map_data(
    embeddings=np.array(plot_embeddings),
    data=data
)
