from openai import OpenAI
from dotenv import dotenv_values

config = dotenv_values(".env")

client = OpenAI(api_key=config["OPENAI_API_KEY"])

response =client.responses.create(
    model="gpt-4.1-mini",
    input="The top 10 most populated cities are: ",
    max_output_tokens=100
)

print(response)