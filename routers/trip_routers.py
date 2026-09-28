from fastapi import APIRouter, Query
from pydantic import BaseModel
from typing import List, Optional

from mock.import_mock_data import get_json_data
from models.DTOs.trip.trip_read import TripRead

trips_mock_data = get_json_data("trips")

class PaginatedTripResponse(BaseModel):
    count: int
    page: int
    size: int
    totalItems: int
    items: List[TripRead]

trip_router = APIRouter(prefix="/trip", tags=["trip"])

@trip_router.get("/trips", response_model=PaginatedTripResponse)
async def trips(
    search: Optional[str] = Query(None, description="Search term for filtering trips"),
    purpose: Optional[str] = Query(None, description="Search term for purpose"),
    page: Optional[int] = Query(1, ge=1, description="Page number for pagination"),
    size: Optional[int] = Query(10, ge=1, le=100, description="Number of items per page"),
):
    """
    Router to list all trips with pagination
    """

    filtered_trips = trips_mock_data
    
    if search:
        filtered_trips = [
            t for t in filtered_trips 
            if search.lower() in t["startAddress"].lower()
        ]

    if purpose:
        filtered_trips = [
            t for t in filtered_trips 
            if t["purpose"] is not None and purpose.lower() == t["purpose"].lower()
        ]

    print("FILTERED TRIPS: " + str(filtered_trips))

    total_items = len(filtered_trips)

    start = (page - 1) * size
    end = start + size
    paginated_items = filtered_trips[start:end]

    return {
        "count": total_items,
        "page": page,
        "size": size,
        "totalItems": total_items,
        "items": paginated_items
    }