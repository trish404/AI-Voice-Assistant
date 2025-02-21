from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

load_dotenv()  
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OpenAI API Key is missing. Set it in the .env file.")

app = FastAPI()

# Define the request model
class UserInput(BaseModel):
    text: str

def chat_with_gpt(text: str):
    openai.api_key = OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}]
    )
    return response["choices"][0]["message"]["content"]

@app.post("/chat")
def chat(user_input: UserInput):
    response = chat_with_gpt(user_input.text)
    return {"response": response}
