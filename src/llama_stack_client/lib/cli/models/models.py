# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import click
from tabulate import tabulate
from llama_stack_client.lib.cli.common.utils import print_table_from_response
from typing import Optional


@click.group()
def models():
    """Query details about available models on Llama Stack distribution."""
    pass


@click.command(name="list", help="Show available llama models at distribution endpoint")
@click.pass_context
def list_models(ctx):
    client = ctx.obj["client"]

    headers = ["identifier", "provider_id", "provider_resource_id", "metadata"]
    response = client.models.list()
    if response:
        print_table_from_response(response, headers)


@click.command(name="get")
@click.argument("model_id")
@click.pass_context
def get_model(ctx, model_id: str):
    """Show available llama models at distribution endpoint"""
    client = ctx.obj["client"]

    models_get_response = client.models.retrieve(identifier=model_id)

    if not models_get_response:
        click.echo(
            f"Model {model_id} is not found at distribution endpoint. "
            "Please ensure endpoint is serving specified model."
        )
        return

    headers = sorted(models_get_response.__dict__.keys())
    rows = []
    rows.append([models_get_response.__dict__[headers[i]] for i in range(len(headers))])

    click.echo(tabulate(rows, headers=headers, tablefmt="grid"))


@click.command(name="register", help="Register a new model at distribution endpoint")
@click.argument("model_id")
@click.option("--provider-id", help="Provider ID for the model", default=None)
@click.option("--provider-model-id", help="Provider's model ID", default=None)
@click.option("--metadata", help="JSON metadata for the model", default=None)
@click.pass_context
def register_model(
    ctx, model_id: str, provider_id: Optional[str], provider_model_id: Optional[str], metadata: Optional[str]
):
    """Register a new model at distribution endpoint"""
    client = ctx.obj["client"]

    try:
        response = client.models.register(
            model_id=model_id, provider_id=provider_id, provider_model_id=provider_model_id, metadata=metadata
        )
        if response:
            click.echo(f"Successfully registered model {model_id}")
    except Exception as e:
        click.echo(f"Failed to register model: {str(e)}")


@click.command(name="update", help="Update an existing model at distribution endpoint")
@click.argument("model_id")
@click.option("--provider-id", help="Provider ID for the model", default=None)
@click.option("--provider-model-id", help="Provider's model ID", default=None)
@click.option("--metadata", help="JSON metadata for the model", default=None)
@click.pass_context
def update_model(
    ctx, model_id: str, provider_id: Optional[str], provider_model_id: Optional[str], metadata: Optional[str]
):
    """Update an existing model at distribution endpoint"""
    client = ctx.obj["client"]

    try:
        response = client.models.update(
            model_id=model_id, provider_id=provider_id, provider_model_id=provider_model_id, metadata=metadata
        )
        if response:
            click.echo(f"Successfully updated model {model_id}")
    except Exception as e:
        click.echo(f"Failed to update model: {str(e)}")


@click.command(name="delete", help="Delete a model from distribution endpoint")
@click.argument("model_id")
@click.pass_context
def delete_model(ctx, model_id: str):
    """Delete a model from distribution endpoint"""
    client = ctx.obj["client"]

    try:
        response = client.models.delete(model_id=model_id)
        if response:
            click.echo(f"Successfully deleted model {model_id}")
    except Exception as e:
        click.echo(f"Failed to delete model: {str(e)}")


# Register subcommands
models.add_command(list_models)
models.add_command(get_model)
models.add_command(register_model)
models.add_command(update_model)
models.add_command(delete_model)
