import click

from .list import list_providers
from .inspect import inspect_provider


@click.group()
def providers():
    """Manage API providers."""


# Register subcommands
providers.add_command(list_providers)
providers.add_command(inspect_provider)
