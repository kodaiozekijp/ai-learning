import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

res = openai.embeddings.create(
    input="dokey tail",
    model="text-embedding-3-small"
)

print(res.data[0].embedding)