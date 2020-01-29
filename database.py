from model import Base, Vehicles
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///database.db?check_same_thread=false&timeout=10&uri=true")
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def addves(name,age,price):
	ves=Vehicles(
		name=name,
		age=age,
		price=price)
	session.add(ves)
	session.commit()
def re_id(id):
   """
   return a product 
   """
   ves = session.query(
      Vehicles).filter_by(id=id).first()
   return ves
def del_id(id):
	session.query(Vehicles).filter_by(id=id).delete()
	session.commit()

def everything():
	ves = session.query(Vehicles).all()
	return ves
	