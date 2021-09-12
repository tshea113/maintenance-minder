from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Car, Service, Base

def open_db(dbName):
  engine = create_engine('sqlite:///' + dbName, echo=True)
  return engine

def close_db(db):
  db.close()
  print("Closed database successfully")

def create_tables(engine):
  Base.metadata.create_all(engine)

def add_car(engine, newMake, newModel, newYear):
  newCar = Car(make=newMake, model=newModel, year=newYear)

  with Session(engine) as session:
    with session.begin():
      session.add(newCar)
    # inner context calls session.commit(), if there were no exceptions
  # outer context calls session.close()

if __name__ == "__main__":
  # an Engine, which the Session will use for connection resources
  engine = open_db('maintenance.db')
  create_tables(engine)

  add_car(engine, 'Mazda', 'Miata', 1993)

  # our_car = session.query(Car).filter_by(make='Mazda').first()
  # print(our_car.car_id)