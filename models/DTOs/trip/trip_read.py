from pydantic import BaseModel

class TripRead(BaseModel):
    tripId: str
    vehicleId: str
    startTime: str
    durationValue: float
    durationUnit: str
    startAddress: str
    endAddress: str
    distanceValue: float
    distanceUnit: str
    tripType: str
    purpose: str | None