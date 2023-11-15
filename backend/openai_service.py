import openai
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import os
import sys

router = APIRouter(
        prefix='/openai_service',
        tags=['openai_service']
        )

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

if not len(OPENAI_API_KEY):
    print("Please set OPENAI_API_KEY environment variable. Exiting.")
    sys.exit(1)

openai.api_key = OPENAI_API_KEY
client_ai = openai.OpenAI()



async def getAnswer(sport, question):
    response = openai.chat.completions.create(
            model = 'gpt-3.5-turbo',
            messages = [
                {'role': 'system', 'content': 'You assist a user by giving information about sports, mostly abour recent sports event, current players, teams and so on. All the discussion is in french' },
                {'role': 'assistant', 'content': 'What do you want to know about ' + sport + '?' },
                {'role': 'user', 'content': question },
                ],
            stream=True,
            max_tokens=100,
            )
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content:
            yield content

class Question(BaseModel):
    question: str

@router.post("{sport_id}")
async def read_sport(sport_id: str, question: Question):
    return StreamingResponse(getAnswer(question.question, sport_id))


