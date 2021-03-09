import uuid
import hashlib

from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

from .base import BaseModel

class Users(BaseModel):
    __tablename__ = 'users'

    username = Column(String(64), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    email = Column(String(64), unique=True, nullable=False)
    first_name = Column(String(100), nullable=True)
    last_name = Column(String(100), nullable=True)
    phone = Column(String(14), unique=True, nullable=True)

    def __repr__(self):
        return f'{self.id} {self.email} {self.username}'

    def __init__(self, username: String, password: String, email: String) -> None:
        self.username = username
        self.password = password
        self.email = email

    # @staticmethod
    # def check_password(hashed_password: str, password: str):
    #     print(1)
    
    @staticmethod
    def hash_password(password: str) -> str:
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

    
