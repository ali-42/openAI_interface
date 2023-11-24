from fastapi import APIRouter, Depends
from models import Dialogs
from sqlalchemy.orm import Session
from sqlalchemy import desc
from typing import Annotated
from database import SessionLocal
from auth import get_current_user

router = APIRouter(
        prefix='/dialogs',
        tags=['dialogs']
        )

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependancy = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.get("/{poetry}")
async def get_dialogs(poetry: str, db: db_dependancy, user: user_dependency):
    dialogs = db.query(Dialogs).filter(Dialogs.poetry == poetry and Dialogs.user_id == user['id']).order_by(desc(Dialogs.created_at)).all()
    return dialogs
    
