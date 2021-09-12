from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Car(Base):
    __tablename__ = "car"
    car_id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    services = relationship("Service", backref=backref("car"))

class Service(Base):
    __tablename__ = "service"
    service_id = Column(Integer, primary_key=True)
    car_id = Column(Integer, ForeignKey("car.car_id"))
    name = Column(String)
    description = Column(String)
    date = Column(Date)
    mileage = Column(Integer)