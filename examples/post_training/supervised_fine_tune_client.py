# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.
# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed in accordance with the terms of the Llama 3 Community License Agreement.

import asyncio
from typing import Optional

import fire
from llama_stack_client import LlamaStackClient

from llama_stack_client.types.post_training_supervised_fine_tune_params import (
    AlgorithmConfigLoraFinetuningConfig,
    TrainingConfig,
    TrainingConfigDataConfig,
    TrainingConfigEfficiencyConfig,
    TrainingConfigOptimizerConfig,
)


async def run_main(
    host: str,
    port: int,
    job_uuid: str,
    model: str,
    use_https: bool = False,
    checkpoint_dir: Optional[str] = None,
    cert_path: Optional[str] = None,
):
    # Construct the base URL with the appropriate protocol
    protocol = "https" if use_https else "http"
    base_url = f"{protocol}://{host}:{port}"

    # Configure client with SSL certificate if provided
    client_kwargs = {"base_url": base_url}
    if use_https and cert_path:
        client_kwargs["verify"] = cert_path

    client = LlamaStackClient(**client_kwargs)

    algorithm_config = AlgorithmConfigLoraFinetuningConfig(
        type="LoRA",
        lora_attn_modules=["q_proj", "v_proj", "output_proj"],
        apply_lora_to_mlp=True,
        apply_lora_to_output=False,
        rank=8,
        alpha=16,
    )

    data_config = TrainingConfigDataConfig(
        dataset_id="alpaca",
        validation_dataset_id="alpaca",
        batch_size=1,
        shuffle=False,
    )

    optimizer_config = TrainingConfigOptimizerConfig(
        optimizer_type="adamw",
        lr=3e-4,
        weight_decay=0.1,
        num_warmup_steps=100,
    )

    effiency_config = TrainingConfigEfficiencyConfig(
        enable_activation_checkpointing=True,
    )

    training_config = TrainingConfig(
        n_epochs=1,
        data_config=data_config,
        efficiency_config=effiency_config,
        optimizer_config=optimizer_config,
        max_steps_per_epoch=30,
        gradient_accumulation_steps=1,
    )

    training_job = client.post_training.supervised_fine_tune(
        job_uuid=job_uuid,
        model=model,
        algorithm_config=algorithm_config,
        training_config=training_config,
        checkpoint_dir=checkpoint_dir,
        # logger_config and hyperparam_search_config haven't been used yet
        logger_config={},
        hyperparam_search_config={},
    )

    print(f"finished the training job: {training_job.job_uuid}")


def main(
    host: str,
    port: int,
    job_uuid: str,
    model: str,
    use_https: bool = False,
    checkpoint_dir: Optional[str] = "null",
    cert_path: Optional[str] = None,
):
    job_uuid = str(job_uuid)
    asyncio.run(run_main(host, port, job_uuid, model, use_https, checkpoint_dir, cert_path))


if __name__ == "__main__":
    fire.Fire(main)
