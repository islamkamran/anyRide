from app.db.db_setup import Base
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum
from datetime import datetime, time
from sqlalchemy import event, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import (
    Float, Column, ForeignKey, Integer, String, DateTime, func, Boolean, Enum,
    JSON, Text
)

class TimestampMixin:
    created_at = Column(DateTime(timezone=True), server_default=func.now(),
                        nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(),
                        onupdate=func.now(), nullable=False)


# User Personal Information
class User(TimestampMixin, Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    firstname = Column(String(255), index=True, nullable=False)
    lastname = Column(String(255), index=True, nullable=False)
    gender = Column(String(25), index=True, nullable=False)
    email = Column(String(255), index=True,  unique=True, nullable=True)
    phonenumber = Column(String(15), unique=True, nullable=True)
    uid = Column(String(255), unique=True, nullable=False)
    original_password = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)

    # Relationships
    customer = relationship("Customer", back_populates="user", uselist=False)
    driver = relationship("Driver", back_populates="user", uselist=False)
    employee = relationship("Employee", back_populates="user", uselist=False)


# ***************** SUB CATEGORIES OF USERS *********************
# User Personal Information
class Customer(TimestampMixin, Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    fk_user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)

    Fav_start_location = Column(String(255), nullable=True)
    Fav_end_location = Column(String(255), nullable=True)

    # Relation Ship
    user = relationship("User", back_populates = "customer")
    rides = relationship("Ride", back_populates="customer")

# User Personal Information
class Driver(TimestampMixin, Base):
    __tablename__ = "drivers"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    fk_user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)

    rating  = Column(Float, nullable=False)
    license_number = Column(String(255), nullable=False)
    experience = Column(String(255), nullable=True)
    total_trips = Column(String(255), nullable=True)
    total_earnings = Column(String(255), nullable=True)
    account_status = Column(String(255), nullable=False)
    is_available = Column(Boolean, nullable=False)  # YES/ NO
    current_location = Column(String(255), nullable=True)

    # Relation Ship
    user = relationship("User", back_populates="driver")
    vehicles = relationship("Vehicle", back_populates="driver")
    rides = relationship("Ride", back_populates="driver") 


# User Personal Information
class Employee(TimestampMixin, Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    fk_user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)

    dob = Column(DateTime, nullable=True)
    emergency_contact = Column(String(255), nullable=False)
    hire_date = Column(DateTime, nullable=True)
    job_title = Column(String(255), nullable=True)
    department = Column(String(255), nullable=True)
    reporting_manager = Column(String(255), nullable=True)
    employment_type = Column(String(255), nullable=True)
    role = Column(String(255), nullable=True)
    salary = Column(Float, nullable=True)
    benefits = Column(String(255), nullable=True)
    performance = Column(String(255), nullable=True)
    skills = Column(String(255), nullable=True)

    # Relation Ship
    user = relationship("User", back_populates="employee")
    


class Vehicle(TimestampMixin, Base):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    fk_driver_id = Column(Integer, ForeignKey("drivers.id"), nullable=False)

    name = Column(String(255), nullable=True)
    color = Column(String(255), nullable=True)
    body_type = Column(String(255), nullable=True)
    make = Column(String(255), nullable=True)
    model = Column(String(255), nullable=True)
    chassis_number = Column(String(255), nullable=True)
    status = Column(String(255), nullable=True)
    description = Column(String(255), nullable=True)
    condition = Column(String(255), nullable=True)
    features = Column(String(255), nullable=True)
    drive_type = Column(String(255), nullable=True)

    # Relation Ship
    driver = relationship("Driver", back_populates="vehicles")
    rides = relationship("Ride", back_populates="vehicle")


class Ride(TimestampMixin, Base):
    __tablename__ = "rides"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    fk_customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    fk_driver_id = Column(Integer, ForeignKey("drivers.id"), nullable=False)
    fk_vehicle_id = Column(Integer, ForeignKey("vehicles.id"), nullable=False)


    ride_category = Column(String(255), nullable=True)
    start_time = Column(DateTime, nullable=True)
    end_time = Column(DateTime, nullable=True)
    base_price = Column(Float, nullable=True)
    ride_price = Column(Float, nullable=True)
    ride_total_price = Column(Float, nullable=True)
    starting_location = Column(String(255), nullable=True)
    ending_location = Column(String(255), nullable=True)

    # Relation Ship
    customer = relationship("Customer", back_populates="rides")
    driver = relationship("Driver", back_populates="rides")
    vehicle = relationship("Vehicle", back_populates="rides")