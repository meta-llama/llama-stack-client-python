import click
import yaml
from rich.console import Console
from ..common.utils import handle_client_errors


@click.command(name="update")
@click.argument("api")
@click.argument("provider_id")
@click.argument("provider_type")
@click.argument("config")
@click.pass_context
@handle_client_errors("update providers")
def update_provider(ctx, api, provider_id, provider_type, config):
    """Show available providers on distribution endpoint"""
    client = ctx.obj["client"]
    console = Console()

    import ast

    config = ast.literal_eval(config)

    providers_response = client.providers.update(
        provider_id=provider_id, provider_type=provider_type, api=api, config=config
    )

    if not providers_response:
        click.secho("Provider not found", fg="red")
        raise click.exceptions.Exit(1)

    console.print(f"provider_id={providers_response.provider_id}")
    console.print(f"provider_type={providers_response.provider_type}")
    console.print("config:")
    for line in yaml.dump(providers_response.config, indent=2).split("\n"):
        console.print(line)
