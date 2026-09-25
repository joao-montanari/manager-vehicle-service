from sqlalchemy import Column, String, Integer, Boolean, Float, ForeignKey
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database_config import Base

class Trip(Base):
    __tablename__ = "trips"

    trip_id = Column("tripId", Integer, primary_key=True, autoincrement=True)
    vehicle_id = Column("vehicleId", String)
    start_time = Column("startTime", String)
    duration_value = Column("durationValue", Float)
    duration_unit = Column("durationUnit", String)
    start_address = Column("startAddress", String)
    end_address = Column("endAddress", String)
    distance_value = Column("distanceValue", Float)
    distance_unit = Column("distanceUnit", String)
    trip_type = Column("tripType", String)
    purpose = Column("purpose", String)
    driver = Column("driver", ForeignKey("users.id"))

    def __init__(
        self,
        vehicle_id,
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
        self.vehicle_id = vehicle_id
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