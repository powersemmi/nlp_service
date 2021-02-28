from .base import BaseModel

from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import TIMESTAMP, INTEGER, VARCHAR

class Employee(BaseModel):
    __tablename__ = 'employees'

    first_name = Column(VARCHAR(255), nullable=False)
    last_name = Column(VARCHAR(255), nullable=False)
    phone = Column(VARCHAR(255), unique=True, nullable=True)
    description = Column(VARCHAR(255), nullable=True)