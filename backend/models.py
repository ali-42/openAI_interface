from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
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
    poetry = Column(String, index=True)
    question = Column(String, index=True)
    answer = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("Users", back_populates="dialogs")
