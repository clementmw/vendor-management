from faker import Faker
from sqlalchemy.orm import sessionmaker
from models import Base,engine,Vendor,Customer,Admin

fake  = Faker()

Session = sessionmaker(bind = engine)
session = Session()

# to delete data from sqldatabase
# session.query(Vendor).delete()
# session.query(Customer).delete()
# session.query(Admin).delete()

# seed data
vendor = [
    Vendor(name = fake.company(),
           product = fake.word(),
           price = fake.random_int(min=10,max=1000)
           )
    for _ in range(5)
]
session.add_all(vendor)

# customer = [
#     Customer(name = fake.name(),
#              location = fake.city()
#              )
#     for _ in range(2)
# ]
# session.add_all(customer)

admin = [
    Admin(name = fake.name(),
          customer_id = fake.random_int(min=1,max=5),
          vendor_id = fake.random_int(min=1,max=5)
          )
    for _ in range(5)
]
session.add_all(admin)

session.commit()


session.close()

