import os
from dotenv import load_dotenv
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# read OPENAI_API_KEY from .env file and save it in environment variable
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class AskModel(BaseModel):
    question: str

@app.post("/ask/")
async def ask(model: AskModel):
    question = model.question
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"{question}"}]
    )

    # read the response from OpenAI API
    answer = chat_completion.choices[0].message.content.strip()
    return answer