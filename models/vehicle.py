from sqlalchemy import Column, String, Integer, Boolean, Float, ForeignKey

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database_config import Base

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    model_year = Column("modelYear", Integer)
    chassis_number = Column("chassisNumber", String)
    license_plate = Column("licensePlate", String)
    initial_mileage = Column("initialMileage", Float)
    first_mileage = Column("firstMileage", Float)
    vtv_expiration = Column("vtvExpiration", String)
    registration_date = Column("registrationDate", String)
    business_area = Column("businessArea", String)
    business_line = Column("businessLine", String)
    market_segment = Column("marketSegment", String)
    use_class = Column("useClass", Boolean)
    expense_group = Column("expenseGroup", String)
    cost_center = Column("costCenter", String)
    version = Column("version", Integer)
    telemetry_capable = Column("telemetryCapable", Boolean)
    document_date = Column("documentDate", String)
    kba_number = Column("kbaNumber", String)
    drivers_name = Column("driversName", String)
    last_mileage_updated = Column("lastMileageUpdated", Float)
    display_model_brand = Column("displayModelBrand", String)
    integration_type = Column("integrationType", String)
    last_telemetry_status = Column("lastTelemetryStatus", String)
    have_maintenance_plan = Column("haveMaintenancePlan", Boolean)
    have_price_table = Column("havePriceTable", Boolean)
    gps_status = Column("gpsStatus", String)
    gps_origin = Column("gpsOrigin", String)
    active = Column("active", Boolean)
    server_url = Column("serverUrl", String)

    def __init__(
        self,
        model_year,
        chassis_number,
        license_plate,
        initial_mileage,
        first_mileage,
        vtv_expiration,
        registration_date,
        business_area,
        business_line,
        market_segment,
        use_class,
        expense_group,
        cost_center,
        version,
        telemetry_capable,
        document_date,
        kba_number,
        drivers_name,
        last_mileage_updated,
        display_model_brand,
        integration_type,
        last_telemetry_status,
        have_maintenance_plan,
        have_price_table,
        gps_status,
        gps_origin,
        active,
        server_url,
    ):
        self.model_year = model_year
        self.chassis_number = chassis_number
        self.license_plate = license_plate
        self.initial_mileage = initial_mileage
        self.first_mileage = first_mileage
        self.vtv_expiration = vtv_expiration
        self.registration_date = registration_date
        self.business_area = business_area
        self.business_line = business_line
        self.market_segment = market_segment
        self.use_class = use_class
        self.expense_group = expense_group
        self.cost_center = cost_center
        self.version = version
        self.telemetry_capable = telemetry_capable
        self.document_date = document_date
        self.kba_number = kba_number
        self.drivers_name = drivers_name
        self.last_mileage_updated = last_mileage_updated
        self.display_model_brand = display_model_brand
        self.integration_type = integration_type
        self.last_telemetry_status = last_telemetry_status
        self.have_maintenance_plan = have_maintenance_plan
        self.have_price_table = have_price_table
        self.gps_status = gps_status
        self.gps_origin = gps_origin
        self.active = active
        self.server_url = server_url