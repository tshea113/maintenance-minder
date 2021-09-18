import db

import datetime

from sqlalchemy.orm import Session

from rich.console import Console
from rich.table import Column, Table

def view_services(engine):
  with Session(engine) as session:
    with session.begin():
      cars = db.get_cars(session)

      print("\nWhich car do you want to view?")
      for index, car in enumerate(cars):
        print(str(index+1) + '. ' + str(car.year) + ' ' + car.make + ' ' + car.model)
      
      print()

      userInput = input()

      services = db.get_services(session, cars[int(userInput)-1])

      console = Console()

      # TODO: Table building probably could be its own function
      table = Table(show_header=True, header_style="bold magenta")
      table.add_column("Date", style="dim", width=12)
      table.add_column("Service")
      table.add_column("Description")
      table.add_column("Mileage")

      for service in services:
        table.add_row(service.date.strftime('%m/%d/%Y'), service.name, service.description, str(service.mileage))

      console.print(table)

def insert_car(engine):
  with Session(engine) as session:
    with session.begin():
      cars = db.get_cars(session)

      print("\nEnter the following information: Year Make Model")

      userInput = input() #TODO: Probably should make this input more robust. Seems like it would break easy

      data = userInput.split()

      db.add_car(session, newYear=data[0], newMake=data[1], newModel=data[2])

  print("\nCar added!") # TODO: This probably should be an actual verification

def insert_service(engine):
  with Session(engine) as session:
    with session.begin():
      cars = db.get_cars(session)

      print("\nWhich car would you like to add a service?")
      for index, car in enumerate(cars):
        print(str(index+1) + '. ' + str(car.year) + ' ' + car.make + ' ' + car.model)
      print()

      userInput = input() #TODO: Probably should make this input more robust. Seems like it would break easy
      car = cars[int(userInput)-1]

      print("\nEnter the name of the service")
      name = input()
      print()

      print("\nEnter the description of the service")
      description = input()
      print()

      print("\nEnter the date of the service in the format MM/DD/YY")
      date = input()
      print()

      print("\nEnter the mileage of the service")
      mileage = input()
      print()

      db.add_service(session, newCar=car, newName=name, newDescription=description, newDate=datetime.datetime.strptime(date, '%m/%d/%y').date(), newMileage=int(mileage))

  print("\nService added!") # TODO: This probably should be an actual verification  