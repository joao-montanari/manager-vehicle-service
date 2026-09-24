from fastapi import APIRouter

trip_router = APIRouter(prefix="/trip", tags=["trip"])

@trip_router.get("/trips")
async def trips():
    """
    Router to list all trips with pagination
    """
    return {
        "message": "you access trips router"
    }