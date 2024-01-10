import click
from seed import session

@click.group #to handle the click groups
def cli():
    pass



@click.command()
def customer():
    name = click.prompt('Enter customer name')
    location = click.prompt('Enter customers location')
    click.echo(f'customers {name}, from {location}, added sucessfully')

@click.command()
def vendor ():
    name = click.prompt('Enter company  name')
    product = click.prompt('Enter vendors product')
    price = click.prompt('Enter products price')
    click.echo(f'company {name}, product {product}, price {price}/= ')

@click.command()
def admin():
    name = click.prompt('Enter admin name')
    click.echo(f'admin {name} added sucessfully')


if __name__ == '__main__':
    cli.add_command(customer)
    cli.add_command(vendor)
    cli.add_command(admin)
    cli()

