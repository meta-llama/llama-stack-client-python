# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from typing import Optional

import click
from rich.console import Console

from ...inference.event_logger import EventLogger
from ..common.utils import handle_client_errors


@click.group()
def inference():
    """Inference (chat)."""


@click.command("chat-completion")
@click.option("--message", required=True, help="Message")
@click.option("--stream", is_flag=True, help="Streaming", default=False)
@click.option("--model-id", required=False, help="Model ID")
@click.pass_context
@handle_client_errors("inference chat-completion")
def chat_completion(ctx, message: str, stream: bool, model_id: Optional[str]):
    """Show available inference chat completion endpoints on distribution endpoint"""
    client = ctx.obj["client"]
    console = Console()

    if not model_id:
        available_models = [model.identifier for model in client.models.list() if model.model_type == "llm"]
        model_id = available_models[0]

    response = client.inference.chat_completion(
        model_id=model_id,
        messages=[{"role": "user", "content": message}],
        stream=stream,
    )
    if not stream:
        console.print(response)
    else:
        for event in EventLogger().log(response):
            event.print()


# Register subcommands
inference.add_command(chat_completion)
