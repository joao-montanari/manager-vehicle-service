from sqlalchemy import Column, String, Integer, Boolean, Float, ForeignKey

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database_config import Base

class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    email = Column("email", String, nullable=False)
    password = Column("password", String)
    active = Column("active", Boolean, default=True)
    role = Column("role", String)

    def __init__(
        self, 
        name, 
        email, 
        password, 
        role, 
        active=True
    ):
        self.name = name
        self.email = email
        self.password = password
        self.active = active
        self.role = role