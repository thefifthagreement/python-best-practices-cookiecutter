import click

from {{cookiecutter.repo_name}}.{{cookiecutter.repo_name}} import fib

@click.command()
@click.argument('n', type=click.INT)
def cli(n: int):
    print(fib(n))
