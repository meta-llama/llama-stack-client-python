import click

from .list import list_providers


@click.group()
def providers():
    """Manage API providers."""


# Register subcommands
providers.add_command(list_providers)
