# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from typing import Optional

import click
from rich.console import Console
from rich.table import Table

from ..common.utils import handle_client_errors


@click.group()
def models():
    """Query details about available models on Llama Stack distribution."""
    pass


@click.command(name="list", help="Show available llama models at distribution endpoint")
@click.pass_context
@handle_client_errors("list models")
def list_models(ctx):
    client = ctx.obj["client"]
    console = Console()

    headers = ["identifier", "provider_id", "provider_resource_id", "metadata"]
    response = client.models.list()
    if response:
        table = Table()
        for header in headers:
            table.add_column(header)

        for item in response:
            table.add_row(
                str(getattr(item, headers[0])),
                str(getattr(item, headers[1])),
                str(getattr(item, headers[2])),
                str(getattr(item, headers[3])),
            )
        console.print(table)


@click.command(name="get")
@click.argument("model_id")
@click.pass_context
@handle_client_errors("get model details")
def get_model(ctx, model_id: str):
    """Show available llama models at distribution endpoint"""
    client = ctx.obj["client"]
    console = Console()

    models_get_response = client.models.retrieve(identifier=model_id)

    if not models_get_response:
        console.print(
            f"Model {model_id} is not found at distribution endpoint. "
            "Please ensure endpoint is serving specified model.",
            style="bold red",
        )
        return

    headers = sorted(models_get_response.__dict__.keys())
    table = Table()
    for header in headers:
        table.add_column(header)

    table.add_row(*[str(models_get_response.__dict__[header]) for header in headers])
    console.print(table)


@click.command(name="register", help="Register a new model at distribution endpoint")
@click.argument("model_id")
@click.option("--provider-id", help="Provider ID for the model", default=None)
@click.option("--provider-model-id", help="Provider's model ID", default=None)
@click.option("--metadata", help="JSON metadata for the model", default=None)
@click.pass_context
@handle_client_errors("register model")
def register_model(
    ctx, model_id: str, provider_id: Optional[str], provider_model_id: Optional[str], metadata: Optional[str]
):
    """Register a new model at distribution endpoint"""
    client = ctx.obj["client"]
    console = Console()

    response = client.models.register(
        model_id=model_id, provider_id=provider_id, provider_model_id=provider_model_id, metadata=metadata
    )
    if response:
        console.print(f"[green]Successfully registered model {model_id}[/green]")


@click.command(name="unregister", help="Unregister a model from distribution endpoint")
@click.argument("model_id")
@click.pass_context
@handle_client_errors("unregister model")
def unregister_model(ctx, model_id: str):
    client = ctx.obj["client"]
    console = Console()

    response = client.models.unregister(model_id=model_id)
    if response:
        console.print(f"[green]Successfully deleted model {model_id}[/green]")


# Register subcommands
models.add_command(list_models)
models.add_command(get_model)
models.add_command(register_model)
models.add_command(unregister_model)
