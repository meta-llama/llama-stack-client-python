# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import click
from typing import Optional
import yaml
from rich.table import Table
from rich.console import Console


@click.group()
def memory_banks():
    """Query details about available memory banks type on distribution."""
    pass


@click.command("list")
@click.pass_context
def list(ctx):
    """Show available memory banks on distribution endpoint"""

    client = ctx.obj["client"]
    console = Console()
    memory_banks_list_response = client.memory_banks.list()
    headers = []
    if memory_banks_list_response and len(memory_banks_list_response) > 0:
        headers = sorted(memory_banks_list_response[0].__dict__.keys())

    if memory_banks_list_response:
        table = Table()
        for header in headers:
            table.add_column(header)

        for item in memory_banks_list_response:
            table.add_row(*[str(getattr(item, header)) for header in headers])
        console.print(table)


@memory_banks.command()
@click.option("--memory-bank-id", required=True, help="Id of the memory bank")
@click.option("--type", type=click.Choice(["vector", "keyvalue", "keyword", "graph"]), required=True)
@click.option("--provider-id", help="Provider ID for the memory bank", default=None)
@click.option("--provider-memory-bank-id", help="Provider's memory bank ID", default=None)
@click.option("--chunk-size", type=int, help="Chunk size in tokens (for vector type)", default=512)
@click.option("--embedding-model", type=str, help="Embedding model (for vector type)", default="all-MiniLM-L6-v2")
@click.option("--overlap-size", type=int, help="Overlap size in tokens (for vector type)", default=64)
@click.pass_context
def create(
    ctx,
    memory_bank_id: str,
    type: str,
    provider_id: Optional[str],
    provider_memory_bank_id: Optional[str],
    chunk_size: Optional[int],
    embedding_model: Optional[str],
    overlap_size: Optional[int],
):
    """Create a new memory bank"""
    client = ctx.obj["client"]

    config = None
    if type == "vector":
        config = {
            "type": "vector",
            "chunk_size_in_tokens": chunk_size,
            "embedding_model": embedding_model,
        }
        if overlap_size:
            config["overlap_size_in_tokens"] = overlap_size
    elif type == "keyvalue":
        config = {"type": "keyvalue"}
    elif type == "keyword":
        config = {"type": "keyword"}
    elif type == "graph":
        config = {"type": "graph"}

    response = client.memory_banks.register(
        memory_bank_id=memory_bank_id,
        params=config,
        provider_id=provider_id,
        provider_memory_bank_id=provider_memory_bank_id,
    )
    if response:
        click.echo(yaml.dump(response.dict()))


# Register subcommands
memory_banks.add_command(list)
memory_banks.add_command(create)
