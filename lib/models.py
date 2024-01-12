from sqlalchemy import create_engine, Integer, Column, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import date

Base = declarative_base()
engine = create_engine('sqlite:///sales.db')  # creates the engine sales

# many -many relationship table
vendor_customer = Table(
    'vendor_customer',
    Base.metadata,
    Column('vendor_id', ForeignKey('vendors.id'), primary_key=True),
    Column('customer_id', ForeignKey('customers.id'), primary_key=True),
    extend_existing=True,
)

class Vendor(Base):
    __tablename__ = 'vendors'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    product = Column(Integer())
    price = Column(Integer())

    admin_id = Column(Integer(), ForeignKey('admins.id'))
    admin = relationship('Admin', back_populates='vendors')

    customers = relationship('Customer', secondary=vendor_customer, back_populates='vendors')

    def __repr__(self):
        return f"Vendor {self.id}. {self.name}, Product: {self.product}, Price: {self.price}"

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    location = Column(String())

    admin_id = Column(Integer(), ForeignKey('admins.id'))
    admin = relationship('Admin', back_populates='customers')

    vendors = relationship('Vendor', secondary=vendor_customer, back_populates='customers')

    def __repr__(self):
        return f"{self.id},  Customer Name:  {self.name}."

class Admin(Base):
    __tablename__ = 'admins'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    created_at = Column(String(), default=date.today())

    customers = relationship('Customer', back_populates='admin')
    vendors = relationship('Vendor', back_populates='admin')

    def __repr__(self):
        return f"Admin Name: {self.name}."
