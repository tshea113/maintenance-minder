from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Car, Service, Base
from datetime import date, datetime

# -----------------------------------------------------------------------------------------------------------------
#
# Database operations
#
# -----------------------------------------------------------------------------------------------------------------
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

# -----------------------------------------------------------------------------------------------------------------
#
# User operations
#
# -----------------------------------------------------------------------------------------------------------------

def view_services():
  with Session(engine) as session:
    with session.begin():
      cars = get_cars(session)

      print("Which car do you want to view?")
      for index, car in enumerate(cars):
        print(str(index+1) + '. ' + str(car.year) + ' ' + car.make + ' ' + car.model)
      
      userInput = input()

      services = get_services(session, cars[int(userInput)-1])

      for service in services:
        print(service.name + ' ' + service.date.strftime('%m/%d/%Y') + ' ' + str(service.mileage))

      print()

if __name__ == "__main__":
  # Initializes the database if it doesn't already exist
  engine = open_db('maintenance.db')
  create_tables(engine)

  while True:
    print('Select an option:\n1. View Service History\n2. Exit')
    userInput = input()
    
    if userInput[0] == '1': view_services()
    elif userInput[0] == '2': break

  # with Session(engine) as session:
  #   with session.begin():

  #     currCar = get_cars(session)[0]

  #     add_service(session, currCar, 'Tires', 'Nitto', date(1901, 2, 1), 70000)