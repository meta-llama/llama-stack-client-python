# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.
import base64
import json
import mimetypes
import os
from typing import Optional

import click
import yaml

from ..common.utils import handle_client_errors


def data_url_from_file(file_path: str) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "rb") as file:
        file_content = file.read()

    base64_content = base64.b64encode(file_content).decode("utf-8")
    mime_type, _ = mimetypes.guess_type(file_path)

    data_url = f"data:{mime_type};base64,{base64_content}"
    return data_url


@click.command("register")
@click.option("--dataset-id", required=True, help="Id of the dataset")
@click.option("--provider-id", help="Provider ID for the dataset", default=None)
@click.option("--provider-dataset-id", help="Provider's dataset ID", default=None)
@click.option("--metadata", type=str, help="Metadata of the dataset")
@click.option("--url", type=str, help="URL of the dataset", required=False)
@click.option(
    "--dataset-path", required=False, help="Local file path to the dataset. If specified, upload dataset via URL"
)
@click.option("--schema", type=str, help="JSON schema of the dataset", required=True)
@click.pass_context
@handle_client_errors("register dataset")
def register(
    ctx,
    dataset_id: str,
    provider_id: Optional[str],
    provider_dataset_id: Optional[str],
    metadata: Optional[str],
    url: Optional[str],
    dataset_path: Optional[str],
    schema: str,
):
    """Create a new dataset"""
    client = ctx.obj["client"]

    try:
        dataset_schema = json.loads(schema)
    except json.JSONDecodeError as err:
        raise click.BadParameter("Schema must be valid JSON") from err

    if metadata:
        try:
            metadata = json.loads(metadata)
        except json.JSONDecodeError as err:
            raise click.BadParameter("Metadata must be valid JSON") from err

    if dataset_path:
        url = data_url_from_file(dataset_path)
    else:
        if not url:
            raise click.BadParameter("URL is required when dataset path is not specified")

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
