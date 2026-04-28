from dotenv import dotenv_values
from fastapi import FastAPI, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import Response
from fastapi.requests import Request
import logging
from openai import OpenAI
from typing import Annotated
import json

logging.basicConfig(level=logging.INFO)

config = dotenv_values(".env")
client = OpenAI(api_key=config["OPENAI_API_KEY"])

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def get_colors(message: str) -> list[str]:
    prompt = f"""
    You are a palette generating assistant that responds to text prompts for color palettes.
    You should generate color palettes that fit the theme, mood, or instructions in the prompt.
    The palettes should be between 2 and 8 colors.

    Q: Convert the following verbal description of a color palette into a list of colors: The Mediterranean Sea.
    A: ["#006699", "#66CCCC", "#F0E68C", "#008000", "#F08080"]

    Q: Convert the following verbal description of a color palette into a list of colors: sage, nature, earth
    A: ["#EDF1D6", "#9DC08B", "#609966", "#40513B"]

    Desired Format: a JSON array of hexadecimal color codes

    Q: Convert the following verbal description of a color palette into a list of colors: {message}
    A:  
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "system", "content": prompt}],
        max_tokens=100
    )
    return json.loads(response.choices[0].message.content)

@app.get("/")
def read_root(request: Request) -> Response:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "system", "content": "give me one funny word"}]
    )
    return response.choices[0].message.content
    # return templates.TemplateResponse(request,"index.html")

@app.post("/palette")
def prompt_to_palette(request: Request, query: Annotated[str, Form()]) -> Response:
    # OPEN AI COMPLETION CALL
    colors = get_colors(query)
    # RETURN LIST OF COLORS
    return {"colors": colors}