from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

db = create_engine("sqlite:///database.db")

Base = declarative_base()


# Step by step to use sqlalchemy

# 1. Create data base connection
# 2. Create a base to data base
# 3. Create data base class/table
# 4. Execute creation method from data base (create data base)