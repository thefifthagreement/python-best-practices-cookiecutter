import click

from bp_test.bp_test import fib


@click.command()
@click.argument("n", type=click.INT)
def cli(n: int):
    print(fib(n))


if __name__ == "__main__":
    cli()
