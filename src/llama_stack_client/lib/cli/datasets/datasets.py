# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import click
import yaml
from typing import Optional
import json

from llama_models.llama3.api.datatypes import URL
from .list import list_datasets


@click.group()
def datasets():
    """Query details about available datasets on Llama Stack distribution."""
    pass


@datasets.command()
@click.option("--dataset-id", required=True, help="Id of the dataset")
@click.option("--provider-id", help="Provider ID for the dataset", default=None)
@click.option("--provider-dataset-id", help="Provider's dataset ID", default=None)
@click.option("--metadata", type=str, help="Metadata of the dataset")
@click.option("--url", type=str, help="URL of the dataset", required=True)
@click.option("--schema", type=str, help="JSON schema of the dataset", required=True)
@click.pass_context
def register(
    ctx,
    dataset_id: str,
    provider_id: Optional[str],
    provider_dataset_id: Optional[str],
    metadata: Optional[str],
    url: str,
    schema: str,
):
    """Create a new dataset"""
    client = ctx.obj["client"]

    try:
        dataset_schema = json.loads(schema)
    except json.JSONDecodeError:
        raise click.BadParameter("Schema must be valid JSON")

    if metadata:
        try:
            metadata = json.loads(metadata)
        except json.JSONDecodeError:
            raise click.BadParameter("Metadata must be valid JSON")

    response = client.datasets.register(
        dataset_id=dataset_id,
        dataset_schema=dataset_schema,
        url={"uri": url},
        provider_id=provider_id,
        provider_dataset_id=provider_dataset_id,
        metadata=metadata,
    )
    if response:
        click.echo(yaml.dump(response.dict()))


# Register subcommands
datasets.add_command(list_datasets)
datasets.add_command(register)
