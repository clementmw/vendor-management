from sqlalchemy import create_engine, Integer, Column,String
from sqlalchemy.ext.declarative import declarative_base

engine  = create_engine('sqlite:///sales.db') #creates the engine sales
Base = declarative_base()


class Vendor:
    __tablename__ = 'vendors'

    id = Column (Integer(),primary_key=True)
    name = Column(String())
    product = Column(Integer())
    price = Column(Integer())

    def __repr__(self):
        return f"vendor{self.id}."\
        f"  {self.name}"\
        f"Product:  {self.product}"\
        f"Price: {self.price}"
        
class Customer:
    __tablename__ = 'customers'

    id  = Column(Integer(),primary_key=True)
    name = Column(String())


    def __repr__(self):
        return f"{self.id},  Customer Name:  {self.name}."
    
class Admin:
    __tablename__ = 'admins'

    id = Column(Integer(),primary_key=True)
    name = Column(String())

    def __repr__ (self):
        return f"Admin Name: {self.name}."
        
    
        

    