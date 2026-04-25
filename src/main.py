from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import Response
from fastapi.requests import Request
from openai import OpenAI
from dotenv import dotenv_values

config = dotenv_values(".env")
client = OpenAI(api_key=config["OPENAI_API_KEY"])

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request) -> Response:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "system", "content": "give me one funny word"}]
    )
    return response.choices[0].message.content
    # return templates.TemplateResponse(request,"index.html")

# @app.post("/palette")
# def prompt_to_palette(request: Request) -> Response:
    # OPEN AI COMPLETION CALL

    # RETURN LIST OF COLORS