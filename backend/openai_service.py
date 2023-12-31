from models import Dialogs
import openai
from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import StreamingResponse
from auth import get_current_user
from pydantic import BaseModel
from typing import Annotated
from database import SessionLocal
from sqlalchemy.orm import Session
import os
import sys
import time

router = APIRouter(
        prefix='/openai_service',
        tags=['openai_service']
        )

user_dependency = Annotated[dict, Depends(get_current_user)]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependancy = Annotated[Session, Depends(get_db)]


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

if not len(OPENAI_API_KEY):
    print("Please set OPENAI_API_KEY environment variable. Exiting.")
    sys.exit(1)

openai.api_key = OPENAI_API_KEY
client_ai = openai.OpenAI()

async def getAnswer(question, poetry, db: db_dependancy, current_user: user_dependency):
    response = openai.chat.completions.create(
            model = 'gpt-3.5-turbo',
            messages = [
                {'role': 'system', 'content': 'Tu es un chatbot qui répond à l\'utilisateur en s\'exprimant uniquement en utilisant la forme poétique suivante : ' + poetry },
                {'role': 'user', 'content': question },
                ],
            stream=True,
            max_tokens=1000,
            )
    answer = ''
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content:
            answer += content.replace('\n', '<br>')
            yield content
    create_dialog_model = Dialogs(
            poetry = poetry,
            question = question,
            answer = answer,
            user_id = current_user['id']
            )
    db.add(create_dialog_model)
    db.commit()
    return


class Question(BaseModel):
    question: str

@router.post("/{poetry_id}")
async def read_poetry(user: user_dependency, poetry_id: str, question: Question, db: db_dependancy):
    return StreamingResponse(getAnswer(question.question, poetry_id, db, user))


