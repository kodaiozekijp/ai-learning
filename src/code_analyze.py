from openai import OpenAI
from dotenv import dotenv_values

config = dotenv_values(".env")
client = OpenAI(api_key=config["OPENAI_API_KEY"])

bubble_sort = """
def sort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
"""

quick_sort = """
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        sort(array, low, pi - 1)
        sort(array, pi + 1, high)
"""

messages = [
    # {"role": "user", "content": f"Caluculate the time complexity of the following function: {bubble_sort}"}
    {"role": "user", "content": f"Caluculate the time complexity of the following function: {quick_sort}"}
]

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages
)

print(response.choices[0].message.content)