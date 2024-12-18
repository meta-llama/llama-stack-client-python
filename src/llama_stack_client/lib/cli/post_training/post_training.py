# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from typing import Optional

import click

from llama_stack_client.types.post_training_supervised_fine_tune_params import (
    AlgorithmConfig,
    TrainingConfig,
)
from rich.console import Console

from ..common.utils import handle_client_errors


@click.group()
def post_training():
    """Query details about available post_training endpoints on distribution."""
    pass


lora_config = AlgorithmConfig(
    type="LoRA",
    lora_attn_modules=["q_proj", "v_proj", "output_proj"],
    apply_lora_to_mlp=True,
    apply_lora_to_output=False,
    rank=8,
    alpha=16,
)

data_config = DataConfig(
    dataset_id="alpaca",
    validation_dataset_id="alpaca",
    batch_size=1,
    shuffle=False,
)

optimizer_config = OptimizerConfig(
    optimizer_type="adamw",
    lr=3e-4,
    lr_min=3e-5,
    weight_decay=0.1,
    num_warmup_steps=100,
)

effiency_config = EfficienctConfig(
    enable_activation_checkpointing=True,
)

training_config = TrainingConfig(
    n_epochs=1,
    data_config=data_config,
    efficient_config=effiency_config,
    optimizer_config=optimizer_config,
    max_steps_per_epoch=30,
    gradient_accumulation_steps=1,
)


@click.command("supervised_fine_tune")
@click.option("--job-uuid", required=True, help="Job UUID")
@click.option("--model", required=True, help="Model ID")
@click.option("--algorithm-config", required=True, help="Algorithm Config")
@click.option("--training-config", required=True, help="Training Config")
@click.option(
    "--checkpoint-dir", required=False, help="Checkpoint Config", default=None
)
@click.pass_context
@handle_client_errors("post_training supervised_fine_tune")
def supervised_fine_tune(
    ctx,
    job_uuid: str,
    model: str,
    algorithm_config: AlgorithmConfig,
    training_config: TrainingConfig,
    checkpoint_dir: Optional[str],
):
    """Kick off a supervised fine tune job"""
    client = ctx.obj["client"]
    console = Console()

    post_training_job = client.post_training.supervised_fine_tune(
        job_uuid=job_uuid,
        model=model,
        algorithm_config=algorithm_config,
        training_config=training_config,
        checkpoint_dir=None,
        # logger_config and hyperparam_search_config haven't been used yet
        logger_config={},
        hyperparam_search_config={},
    )
    console.print(post_training_job.job_uuid)


@click.command("list")
@click.pass_context
@handle_client_errors("post_training get_training_jobs")
def get_training_jobs(ctx):
    """Show the list of available post training jobs"""
    client = ctx.obj["client"]
    console = Console()

    training_jobs = client.post_training.job.list()
    console.print([training_job.job_uuid for training_job in training_jobs])


@click.command("status")
@click.option("--job-uuid", required=True, help="Job UUID")
@click.pass_context
@handle_client_errors("post_training get_training_job_status")
def get_training_job_status(ctx, job_uuid: str):
    """Show the status of a specific post training job"""
    client = ctx.obj["client"]
    console = Console()

    job_status_reponse = client.post_training.job.status(job_uuid=job_uuid)
    console.print(job_status_reponse)


@click.command("artifacts")
@click.option("--job-uuid", required=True, help="Job UUID")
@click.pass_context
@handle_client_errors("post_training get_training_job_artifacts")
def get_training_job_artifacts(ctx, job_uuid: str):
    """Get the training artifacts of a specific post training job"""
    client = ctx.obj["client"]
    console = Console()

    job_artifacts = client.post_training.job.artifacts(job_uuid=job_uuid)
    console.print(job_artifacts)


@click.command("cancel")
@click.option("--job-uuid", required=True, help="Job UUID")
@click.pass_context
@handle_client_errors("post_training cancel_training_job")
def cancel_training_job(ctx, job_uuid: str):
    """Cancel the training job"""
    client = ctx.obj["client"]

    client.post_training.job.cancel(job_uuid=job_uuid)


# Register subcommands
post_training.add_command(supervised_fine_tune)
post_training.add_command(get_training_jobs)
post_training.add_command(get_training_job_status)
post_training.add_command(get_training_job_artifacts)
post_training.add_command(cancel_training_job)
