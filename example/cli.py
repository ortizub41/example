import click

@click.command()
def cli():
    click.echo("Hello, Everyone!")

if __name__ == '__main__':
    cli()
