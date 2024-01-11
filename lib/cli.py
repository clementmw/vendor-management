import click
from seed import session
from models import Customer,Vendor,Admin

@click.group #to handle the click groups
def cli():
    pass



@click.command()
def customer():
    admin= click.prompt('enter admin id')
    name = click.prompt('Enter customer name')
    location = click.prompt('Enter customers location')

    new_customer  = Customer(name = name, location = location, admin_id=admin)
    session.add(new_customer)
    session.commit()

    click.echo(f'customers {name}, from {location}, added sucessfully')

@click.command()
def vendor ():
    name = click.prompt('Enter company  name')
    product = click.prompt('Enter vendors product')
    price = click.prompt('Enter products price')

    new_vendor  = Vendor(name = name, product = product, price = price)
    session.add(new_vendor)
    session.commit()

    click.echo(f'company {name}, product {product}, price {price}/= ')

@click.command()
def admin():
    name = click.prompt('Enter admin name')
    
    new_admin = Admin(name = name)

    session.add(new_admin)
    session.commit()

    click.echo(f'admin {name} added sucessfully')


if __name__ == '__main__':
    cli.add_command(customer)
    cli.add_command(vendor)
    cli.add_command(admin)
    cli()

