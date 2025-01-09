import click

from .version import inspect_version


@click.group()
def inspect():
    """Query details about available versions on Llama Stack distribution."""
    pass


# Register subcommands
inspect.add_command(inspect_version)
