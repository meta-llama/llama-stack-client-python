# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import click
from llama_stack_client import LlamaStackClient

# from .configure import configure
from .datasets import datasets
from .eval_tasks import eval_tasks
from .memory_banks import memory_banks
from .models import models

from .providers import providers
from .scoring_functions import scoring_functions

from .shields import shields


@click.group()
@click.option("--endpoint", type=str, help="Llama Stack distribution endpoint", default="http://localhost:5000")
@click.pass_context
def cli(ctx, endpoint: str):
    """Welcome to the LlamaStackClient CLI"""
    ctx.ensure_object(dict)
    client = LlamaStackClient(
        base_url=endpoint,
    )
    ctx.obj = {"client": client}


# Register all subcommands
cli.add_command(models, "models")
cli.add_command(memory_banks, "memory_banks")
cli.add_command(shields, "shields")
cli.add_command(eval_tasks, "eval_tasks")
cli.add_command(providers, "providers")
cli.add_command(datasets, "datasets")
cli.add_command(scoring_functions, "scoring_functions")


def main():
    cli()


if __name__ == "__main__":
    main()
