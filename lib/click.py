import click
# from faker import Faker
from sqlalchemy.orm import sessionmaker
from models import Base,engine,Vendor,Customer,Admin

fake  = Faker()

Session = sessionmaker(bind = engine)
session = Session()


session.commit()


session.close()

