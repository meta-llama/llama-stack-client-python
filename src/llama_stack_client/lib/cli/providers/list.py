import click
from tabulate import tabulate


@click.command("list")
@click.pass_context
def list_providers(ctx):
    """Show available providers on distribution endpoint"""
    client = ctx.obj["client"]

    headers = ["API", "Provider ID", "Provider Type"]

    providers_response = client.providers.list()
    rows = []

    for k, v in providers_response.items():
        for provider_info in v:
            rows.append([k, provider_info.provider_id, provider_info.provider_type])

    click.echo(tabulate(rows, headers=headers, tablefmt="grid"))
