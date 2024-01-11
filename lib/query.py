from seed import session
from models import Customer,Admin,Vendor


def query_vendors_and_customers():
    # Query all vendors and their associated customers
    vendors = session.query(Vendor).all()

    for vendor in vendors:
        print(f"\nVendor: {vendor.name}, Product: {vendor.product}, Price: {vendor.price}")
        print("Customers:")
        for customer in vendor.customers:
            print(f"  - {customer.name}")

def query_customers_and_vendors():
    # Query all customers and their associated vendors
    customers = session.query(Customer).all()

    for customer in customers:
        print(f"\nCustomer: {customer.name}, Location: {customer.location}")
        print("Vendors:")
        for vendor in customer.vendors:
            print(f"  - {vendor.name}, Product: {vendor.product}, Price: {vendor.price}")

def query_admins():
    # Query all admins and their associated customers and vendors
    admins = session.query(Admin).all()

    for admin in admins:
        print(f"\nAdmin: {admin.name}")
        print("Customers:")
        for customer in admin.customers:
            print(f"  - {customer.name}")
        print("Vendors:")
        for vendor in admin.vendors:
            print(f"  - {vendor.name}")

if __name__ == "__main__":
    query_vendors_and_customers()
    query_customers_and_vendors()
    query_admins()

session.close()
