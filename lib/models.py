from sqlalchemy import create_engine, Integer, Column, String, ForeignKey,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()
engine  = create_engine('sqlite:///sales.db') #creates the engine sales

# relatioship table
vendor_customer = Table(
    'vendor_customer',
    Base.metadata,
    Column('vendor_id',  ForeignKey('vendors.id'),primary_key=True),
    Column('customer_id',ForeignKey('customers.id'),primary_key=True),
    extend_existing=True,

)


class Vendor(Base):
    __tablename__ = 'vendors'

    id = Column (Integer(),primary_key=True)
    name = Column(String())
    product = Column(Integer())
    price = Column(Integer())

# connection to admin
    admin_id = Column(Integer(), ForeignKey('admins.id'))
    
# connection to customer
    customer = relationship('Customer',secondary=vendor_customer,back_populates='vendor')
    
    

    def __repr__(self):
        return f"vendor{self.id}."\
        f"  {self.name}"\
        f"Product:  {self.product}"\
        f"Price: {self.price}"
        
class Customer(Base):
    __tablename__ = 'customers'

    id  = Column(Integer(),primary_key=True)
    name = Column(String())
    location = Column(String())
# connection to admin
    admin_id = Column(Integer(), ForeignKey('admins.id'))
# connection to vendor
    vendor = relationship('Vendor',secondary=vendor_customer,back_populates='customer')


# represent data 
    def __repr__(self):
        return f"{self.id},  Customer Name:  {self.name}."
    
class Admin(Base):
    __tablename__ = 'admins'

    id = Column(Integer(),primary_key=True)
    name = Column(String())

# establish connection to both vendor and customer 
    customer = relationship('Customer',backref='admin')
    vendor = relationship('Vendor',backref='admin')
    
    def __repr__ (self):
        return f"Admin Name: {self.name}."


# Base.metadata.create_all(engine)
    
        

    