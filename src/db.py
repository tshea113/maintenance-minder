from sqlalchemy import create_engine
from models import Car, Service, Base

def open_db(dbName):
  engine = create_engine('sqlite:///' + dbName)
  
  return engine

def close_db(db):
  db.close()
  print("Closed database successfully")

def create_tables(engine):
  Base.metadata.create_all(engine)

def add_car(session, newMake, newModel, newYear):
  newCar = Car(make=newMake, model=newModel, year=newYear)
  session.add(newCar)
  
  return newCar

def add_service(session, newCar, newName, newDescription, newDate, newMileage):
  newService = Service(name=newName, description=newDescription, date=newDate, mileage=newMileage, car=newCar)
  session.add(newService)
  
  return newService

def get_cars(session):
  cars = session.query(Car).order_by(Car.car_id)
  
  return cars

def get_services(session, car):
  services = session.query(Service).where(Service.car == car).order_by(Service.date)
  
  return services