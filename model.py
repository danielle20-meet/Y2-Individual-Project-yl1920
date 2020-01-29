from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class Vehicles(Base):
	__tablename__ ="Vehicles"
	name= Column(String)
	age=Column(Float)
	price=Column(Float)
	id =Column(Integer,primary_key=True)