# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from typing import Optional

import click

from llama_stack_client.types import post_training_supervised_fine_tune_params
from rich.console import Console

from ..common.utils import handle_client_errors


@click.group()
def post_training():
    """Query details about available post_training endpoints on distribution."""
    pass


lora_config = (
    post_training_supervised_fine_tune_params.AlgorithmConfigLoraFinetuningConfig(
        lora_attn_modules=["q_proj", "v_proj", "output_proj"],
        apply_lora_to_mlp=True,
        apply_lora_to_output=False,
        rank=8,
        alpha=16,
    )
)

data_config = post_training_supervised_fine_tune_params.DataConfig(
    dataset_id="alpaca",
    batch_size=1,
    shuffle=False,
)

optimizer_config = post_training_supervised_fine_tune_params.OptimizerConfig(
    optimizer_type="adamw",
    lr=3e-4,
    lr_min=3e-5,
    weight_decay=0.1,
    num_warmup_steps=100,
)

effiency_config = post_training_supervised_fine_tune_params.EfficienctConfig(
    enable_activation_checkpointing=True,
)

training_config = post_training_supervised_fine_tune_params.TrainingConfig(
    n_epochs=1,
    data_config=data_config,
    efficient_config=effiency_config,
    optimizer_config=optimizer_config,
    max_steps_per_epoch=10,
    gradient_accumulation_steps=1,
)


@click.command("supervised_fine_tune")
@click.pass_context
@handle_client_errors("post_training supervised_fine_tune")
def supervised_fine_tune(ctx):
    """Kick off a supervised fine tune job"""
    client = ctx.obj["client"]
    console = Console()

    post_training_job = client.post_training.supervised_fine_tune(
        job_uuid="1234",
        model="Llama3.2-3B-Instruct",
        algorithm_config=lora_config,
        training_config=training_config,
    )
    console.print(post_training_job.job_uuid)


@click.command("get_training_jobs")
@click.pass_context
@handle_client_errors("post_training get_training_jobs")
def get_training_jobs(ctx):
    """Show the list of available post training jobs"""
    client = ctx.obj["client"]
    console = Console()

    training_jobs = client.post_training.get_training_jobs()
    console.print([training_job.job_uuid for training_job in training_jobs])


@click.command("get_training_job_status")
@click.pass_context
@handle_client_errors("post_training get_training_job_status")
def get_training_job_status(ctx):
    """Show the status of a specific post training job"""
    client = ctx.obj["client"]
    console = Console()

    job_status_reponse = client.post_training.get_training_job_status(job_uuid="1234")
    console.print(job_status_reponse)


@click.command("get_training_job_artifacts")
@click.pass_context
@handle_client_errors("post_training get_training_job_artifacts")
def get_training_job_artifacts(ctx):
    """Get the training artifacts of a specific post training job"""
    client = ctx.obj["client"]
    console = Console()

    job_artifacts = client.post_training.get_training_job_artifacts(job_uuid="1234")
    console.print(job_artifacts)


# Register subcommands
post_training.add_command(supervised_fine_tune)
post_training.add_command(get_training_jobs)
post_training.add_command(get_training_job_status)
post_training.add_command(get_training_job_artifacts)
