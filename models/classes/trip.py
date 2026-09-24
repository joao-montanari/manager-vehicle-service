from sqlalchemy import Column, String, Integer, Boolean, Float, ForeignKey
from ..main import Base

class Trip(Base):
    __tablename__ = "trips"

    trip_id = Column("tripId", Integer, primary_key=True, autoincrement=True)
    start_time = Column("startTime", String)
    duration_value = Column("durationValue", Float)
    duration_unit = Column("durationUnit", String)
    start_address = Column("startAddress", String)
    end_address = Column("endAddress", String)
    distance_value = Column("distanceValue", Float)
    distance_unit = Column("distanceUnit", String)
    trip_type = Column("tripType", String)
    purpose = Column("purpose", String)
    driver = Column("driver", ForeignKey("user.id"))

    def __init__(
        self,
        start_time,
        duration_value,
        duration_unit,
        start_address,
        end_address,
        distance_value,
        distance_unit,
        trip_type,
        purpose,
        driver
    ):
        self.start_time = start_time
        self.duration_value = duration_value
        self.duration_unit = duration_unit
        self.start_address = start_address
        self.end_address = end_address
        self.distance_value = distance_value
        self.distance_unit = distance_unit
        self.trip_type = trip_type
        self.purpose = purpose
        self.driver = driver