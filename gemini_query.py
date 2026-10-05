from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=TOKEN)


def get_embed(text):
    result = client.models.embed_content(
        model="gemini-embedding-2",
        contents=text
    )
    return result.embeddings[0].values
