from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    password = Column(String, index=True)

    dialogs = relationship("Dialogs", back_populates="user")

class Dialogs(Base):
    __tablename__ = 'dialogs'

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    poetry = Column(String, index=True)
    question = Column(String, index=True)
    answer = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("Users", back_populates="dialogs")
