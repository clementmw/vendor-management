import click

@click.command()

@click.option('--name', '-n', default = 'mike', help = 'enter name')

def hello(name):
    click.echo(f'Hello {name}')


if __name__ == '__main__':
    hello()

