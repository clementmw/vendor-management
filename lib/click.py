# import click
from sqlalchemy.orm import sessionmaker
from models import Base,engine,Vendor,Customer,Admin

Session = sessionmaker(bind = engine)
session = Session()
session.commit()
session.close()

