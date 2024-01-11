from faker import Faker
from sqlalchemy.orm import sessionmaker
from models import Base, engine, Vendor, Customer, Admin, vendor_customer

fake = Faker()

Session = sessionmaker(bind=engine)

with Session() as session:
    # seed data for Admin
    admin_names = set()
    admins = []
    for _ in range(5):
        admin_name = fake.name()
        if admin_name not in admin_names:
            admin_names.add(admin_name)
            admins.append(Admin(name=admin_name))
    session.add_all(admins)
    session.commit()

    # seed data for Vendors
    for _ in range(5):
        vendor = Vendor(
            name=fake.company(),
            product=fake.word(),
            price=fake.random_int(min=10, max=1000),
            admin_id=fake.random_int(min=1, max=5)
        )
        session.add(vendor)
    session.commit()

    # seed data for Customers
    for _ in range(5):
        customer = Customer(
            name=fake.name(),
            location=fake.city(),
            admin_id=fake.random_int(min=1, max=5)
        )
        session.add(customer)
    session.commit()
