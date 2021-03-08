import uuid
import hashlib

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import String

from sqlalchemy.sql.schema import MetaData
from .base import BaseModel, db

class Users(BaseModel):
    __tablename__ = 'users'

    username = db.Column(String(64), unique=True, nullable=False)
    password = db.Column(String(120), nullable=False)
    email = db.Column(String(64), unique=True, nullable=False)
    first_name = db.Column(String(100), nullable=True)
    last_name = db.Column(String(100), nullable=True)
    phone = db.Column(String(14), unique=True, nullable=True)

    def __repr__(self):
        return f'{self.id} {self.email} {self.username}'

    def __init__(self, username: String, password: String, email: String) -> None:
        self.username = username
        self.password = password
        self.email = email

    # @staticmethod
    # def check_password(hashed_password: str, password: str):
    #     print(1)
    
    # @staticmethod
    # def hash_password(password):
    #     salt = uuid.uuid4().hex
    #     return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

    
