from fastapi import FastAPI

app = FastAPI()

# Import app routers
from routers.auth_routers import auth_router
from routers.trip_routers import trip_router

app.include_router(auth_router)
app.include_router(trip_router)

# SQLALCHEMY use a ORM concept: transform python class in entity inside data base

# To run: uvicorn main:app --reload