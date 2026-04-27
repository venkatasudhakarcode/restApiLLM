from fastapi import FastAPI
from openai import OpenAI


import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  

settings = Settings()




app = FastAPI()
client = OpenAI(api_key=settings.OPENAI_API_KEY)


@app.get("/")
def home():
    return "Welcome to My World"

@app.post("/chat")
def chat(message: str):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages = [
            {"role":"user", "content":message}
            ]
    )

    return {
        "user_query":message,
        "Ai_response":response.choices[0].message.content
    }