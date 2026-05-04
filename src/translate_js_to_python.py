from openai import OpenAI
from dotenv import dotenv_values

config = dotenv_values(".env")
client = OpenAI(api_key=config["OPENAI_API_KEY"])

js = """
const mystery = (str) => {
    const arr = str.trim().toLowerCased().split(" ");

    for (let i = 0; i < arr.length; i++) {
        arr[i] = arr[i].charAt(0).toUpperCase() + arr[i].slice(1);
    }

    return arr.join(" ");
};
"""

messages = [
    {"role": "user", "content": f"Translate the following JavaScript code to Python: {js}"}
]

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages
)

print(response.choices[0].message.content)