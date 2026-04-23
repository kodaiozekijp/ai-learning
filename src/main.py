from openai import OpenAI
from dotenv import dotenv_values

config = dotenv_values(".env")

client = OpenAI(api_key=config["OPENAI_API_KEY"])

input_text = """
Yout are a chatbot that speaks like a toddler.

User: Hi, how are you?
Chatbot: I'm good
User: Tell me about your family
Chatbot: I have a mommy and a daddy and two kittens
User: What do you do for fun?
Chatbot:
"""

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[{"role": "system", "content": input_text}],
    max_tokens=100,
    stop=["Chatbot:","User:"]
)

print(response.choices[0].message.content)