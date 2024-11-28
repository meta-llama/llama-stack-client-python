# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from typing import Optional

import click
from rich.console import Console

from ..common.utils import handle_client_errors


@click.group()
def post_training():
    """Query details about available post_training endpoints on distribution."""
    pass


@click.command("supervised_fine_tune")
@click.pass_context
@handle_client_errors("post_training supervised_fine_tune")
def supervised_fine_tune(ctx):
    """Show available post_training supervies finetune endpoints on distribution endpoint"""
    client = ctx.obj["client"]
    console = Console()

    post_training_job = client.post_training.supervised_fine_tune(
        dataset_id="alpaca",
        job_uuid="1234",
        model="meta-llama/Llama-3.2-3B-Instruct",
        validation_dataset_id="alpaca",
    )
    console.print(post_training_job.job_uuid)


# Register subcommands
post_training.add_command(supervised_fine_tune)
