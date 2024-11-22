import click
from rich.console import Console
from rich.table import Table

from ..common.utils import handle_client_errors


@click.command("list")
@click.pass_context
@handle_client_errors("list providers")
def list_providers(ctx):
    """Show available providers on distribution endpoint"""
    client = ctx.obj["client"]
    console = Console()
    headers = ["API", "Provider ID", "Provider Type"]

    providers_response = client.providers.list()
    table = Table()
    for header in headers:
        table.add_column(header)

    for k, v in providers_response.items():
        for provider_info in v:
            table.add_row(k, provider_info.provider_id, provider_info.provider_type)

    console.print(table)
