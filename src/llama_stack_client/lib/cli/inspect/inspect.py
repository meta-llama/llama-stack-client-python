import click

from .version import inspect_version


@click.group()
def inspect():
    """Inspect server configuration."""


# Register subcommands
inspect.add_command(inspect_version)
