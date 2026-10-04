from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=TOKEN)

result = client.models.embed_content(
        model="gemini-embedding-2",
        contents="What is the meaning of life?"
)