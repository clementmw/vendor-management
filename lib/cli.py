import click
from seed import session

@click.group #to handle the click groups
def cli():
    pass



@click.command()
def hello():
    vendor= click.prompt('Enter vendor name')
    click.echo(f'vendor {vendor} added sucessfully')

@click.command()
def product ():
    product = click.prompt('Enter product name')
    click.echo(f'product {product} added sucessfully')


if __name__ == '__main__':
    cli.add_command(hello)
    cli.add_command(product)
    cli()

