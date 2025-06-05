import click

from .list import list_providers
from .inspect import inspect_provider
from .update import update_provider


@click.group()
@click.help_option("-h", "--help")
def providers():
    """Manage API providers."""


# Register subcommands
providers.add_command(list_providers)
providers.add_command(inspect_provider)
providers.add_command(update_provider)
