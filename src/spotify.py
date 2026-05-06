import openai
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

def generate_playlist(prompt, count=5):
    example_json = """
    [
        {"song": "Tears Dry On Their Own", "artist": "Amy Winehouse"},
        {"song": "Hurt", "artist": "Nine Inch Nails"},
        {"song": "Someone Like You", "artist": "Adele"},
        {"song": "The Night We Met", "artist": "Lord Huron"},
        {"song": "Fix You", "artist": "Coldplay"}
    ]
    """

    messages = [
        {"role": "system", "content": """You are a helpful playlist generating assistant.
        You should generate a list of songs and their artists according to a text prompt.
        You should return a JSON array, where each elements follows this format: {"song": <song_title>, "artist": <artist_name>}
        """},
        {"role": "user", "content": "Generate a 5 playlist of songs based on this prompt: super super sad songs"},
        {"role": "assistant", "content": example_json},
        {"role": "user", "content": f"Generate a {count} playlist of songs based on this prompt: {prompt}"}
    ]

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=400
    )

    return json.loads(response.choices[0].message.content)

def get_spotify():
    sp = spotipy.Spotify(
         auth_manager=SpotifyOAuth(
            client_id=config["SPOTIFY_CLIENT_ID"],
            client_secret=config["SPOTIFY_CLIENT_SECRET"],
            redirect_uri="http://127.0.0.1:9999/callback",
            scope="user-read-private"
        )
    )

    return sp.search(q="Uptown Funk", type="track", limit=1)

print(get_spotify())