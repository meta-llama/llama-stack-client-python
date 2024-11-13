import click

from .list import list_providers


@click.group()
def providers():
    """Query details about available providers on Llama Stack distribution."""
    pass


# Register subcommands
providers.add_command(list_providers)
