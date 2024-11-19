# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types import (
    PostTrainingJob,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPostTraining:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_preference_optimize(self, client: LlamaStackClient) -> None:
        post_training = client.post_training.preference_optimize(
            algorithm="dpo",
            algorithm_config={
                "epsilon": 0,
                "gamma": 0,
                "reward_clip": 0,
                "reward_scale": 0,
            },
            dataset_id="dataset_id",
            finetuned_model="https://example.com",
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            optimizer_config={
                "lr": 0,
                "lr_min": 0,
                "optimizer_type": "adam",
                "weight_decay": 0,
            },
            training_config={
                "batch_size": 0,
                "enable_activation_checkpointing": True,
                "fsdp_cpu_offload": True,
                "memory_efficient_fsdp_wrap": True,
                "n_epochs": 0,
                "n_iters": 0,
                "shuffle": True,
            },
            validation_dataset_id="validation_dataset_id",
        )
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @parametrize
    def test_method_preference_optimize_with_all_params(self, client: LlamaStackClient) -> None:
        post_training = client.post_training.preference_optimize(
            algorithm="dpo",
            algorithm_config={
                "epsilon": 0,
                "gamma": 0,
                "reward_clip": 0,
                "reward_scale": 0,
            },
            dataset_id="dataset_id",
            finetuned_model="https://example.com",
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            optimizer_config={
                "lr": 0,
                "lr_min": 0,
                "optimizer_type": "adam",
                "weight_decay": 0,
            },
            training_config={
                "batch_size": 0,
                "enable_activation_checkpointing": True,
                "fsdp_cpu_offload": True,
                "memory_efficient_fsdp_wrap": True,
                "n_epochs": 0,
                "n_iters": 0,
                "shuffle": True,
            },
            validation_dataset_id="validation_dataset_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @parametrize
    def test_raw_response_preference_optimize(self, client: LlamaStackClient) -> None:
        response = client.post_training.with_raw_response.preference_optimize(
            algorithm="dpo",
            algorithm_config={
                "epsilon": 0,
                "gamma": 0,
                "reward_clip": 0,
                "reward_scale": 0,
            },
            dataset_id="dataset_id",
            finetuned_model="https://example.com",
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            optimizer_config={
                "lr": 0,
                "lr_min": 0,
                "optimizer_type": "adam",
                "weight_decay": 0,
            },
            training_config={
                "batch_size": 0,
                "enable_activation_checkpointing": True,
                "fsdp_cpu_offload": True,
                "memory_efficient_fsdp_wrap": True,
                "n_epochs": 0,
                "n_iters": 0,
                "shuffle": True,
            },
            validation_dataset_id="validation_dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post_training = response.parse()
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @parametrize
    def test_streaming_response_preference_optimize(self, client: LlamaStackClient) -> None:
        with client.post_training.with_streaming_response.preference_optimize(
            algorithm="dpo",
            algorithm_config={
                "epsilon": 0,
                "gamma": 0,
                "reward_clip": 0,
                "reward_scale": 0,
            },
            dataset_id="dataset_id",
            finetuned_model="https://example.com",
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            optimizer_config={
                "lr": 0,
                "lr_min": 0,
                "optimizer_type": "adam",
                "weight_decay": 0,
            },
            training_config={
                "batch_size": 0,
                "enable_activation_checkpointing": True,
                "fsdp_cpu_offload": True,
                "memory_efficient_fsdp_wrap": True,
                "n_epochs": 0,
                "n_iters": 0,
                "shuffle": True,
            },
            validation_dataset_id="validation_dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post_training = response.parse()
            assert_matches_type(PostTrainingJob, post_training, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_supervised_fine_tune(self, client: LlamaStackClient) -> None:
        post_training = client.post_training.supervised_fine_tune(
            algorithm="full",
            algorithm_config={
                "alpha": 0,
                "apply_lora_to_mlp": True,
                "apply_lora_to_output": True,
                "lora_attn_modules": ["string"],
                "rank": 0,
            },
            dataset_id="dataset_id",
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            model="model",
            optimizer_config={
                "lr": 0,
                "lr_min": 0,
                "optimizer_type": "adam",
                "weight_decay": 0,
            },
            training_config={
                "batch_size": 0,
                "enable_activation_checkpointing": True,
                "fsdp_cpu_offload": True,
                "memory_efficient_fsdp_wrap": True,
                "n_epochs": 0,
                "n_iters": 0,
                "shuffle": True,
            },
            validation_dataset_id="validation_dataset_id",
        )
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @parametrize
    def test_method_supervised_fine_tune_with_all_params(self, client: LlamaStackClient) -> None:
        post_training = client.post_training.supervised_fine_tune(
            algorithm="full",
            algorithm_config={
                "alpha": 0,
                "apply_lora_to_mlp": True,
                "apply_lora_to_output": True,
                "lora_attn_modules": ["string"],
                "rank": 0,
            },
            dataset_id="dataset_id",
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            model="model",
            optimizer_config={
                "lr": 0,
                "lr_min": 0,
                "optimizer_type": "adam",
                "weight_decay": 0,
            },
            training_config={
                "batch_size": 0,
                "enable_activation_checkpointing": True,
                "fsdp_cpu_offload": True,
                "memory_efficient_fsdp_wrap": True,
                "n_epochs": 0,
                "n_iters": 0,
                "shuffle": True,
            },
            validation_dataset_id="validation_dataset_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @parametrize
    def test_raw_response_supervised_fine_tune(self, client: LlamaStackClient) -> None:
        response = client.post_training.with_raw_response.supervised_fine_tune(
            algorithm="full",
            algorithm_config={
                "alpha": 0,
                "apply_lora_to_mlp": True,
                "apply_lora_to_output": True,
                "lora_attn_modules": ["string"],
                "rank": 0,
            },
            dataset_id="dataset_id",
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            model="model",
            optimizer_config={
                "lr": 0,
                "lr_min": 0,
                "optimizer_type": "adam",
                "weight_decay": 0,
            },
            training_config={
                "batch_size": 0,
                "enable_activation_checkpointing": True,
                "fsdp_cpu_offload": True,
                "memory_efficient_fsdp_wrap": True,
                "n_epochs": 0,
                "n_iters": 0,
                "shuffle": True,
            },
            validation_dataset_id="validation_dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post_training = response.parse()
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @parametrize
    def test_streaming_response_supervised_fine_tune(self, client: LlamaStackClient) -> None:
        with client.post_training.with_streaming_response.supervised_fine_tune(
            algorithm="full",
            algorithm_config={
                "alpha": 0,
                "apply_lora_to_mlp": True,
                "apply_lora_to_output": True,
                "lora_attn_modules": ["string"],
                "rank": 0,
            },
            dataset_id="dataset_id",
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            model="model",
            optimizer_config={
                "lr": 0,
                "lr_min": 0,
                "optimizer_type": "adam",
                "weight_decay": 0,
            },
            training_config={
                "batch_size": 0,
                "enable_activation_checkpointing": True,
                "fsdp_cpu_offload": True,
                "memory_efficient_fsdp_wrap": True,
                "n_epochs": 0,
                "n_iters": 0,
                "shuffle": True,
            },
            validation_dataset_id="validation_dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post_training = response.parse()
            assert_matches_type(PostTrainingJob, post_training, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPostTraining:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_preference_optimize(self, async_client: AsyncLlamaStackClient) -> None:
        post_training = await async_client.post_training.preference_optimize(
            algorithm="dpo",
            algorithm_config={
                "epsilon": 0,
                "gamma": 0,
                "reward_clip": 0,
                "reward_scale": 0,
            },
            dataset_id="dataset_id",
            finetuned_model="https://example.com",
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            optimizer_config={
                "lr": 0,
                "lr_min": 0,
                "optimizer_type": "adam",
                "weight_decay": 0,
            },
            training_config={
                "batch_size": 0,
                "enable_activation_checkpointing": True,
                "fsdp_cpu_offload": True,
                "memory_efficient_fsdp_wrap": True,
                "n_epochs": 0,
                "n_iters": 0,
                "shuffle": True,
            },
            validation_dataset_id="validation_dataset_id",
        )
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @parametrize
    async def test_method_preference_optimize_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        post_training = await async_client.post_training.preference_optimize(
            algorithm="dpo",
            algorithm_config={
                "epsilon": 0,
                "gamma": 0,
                "reward_clip": 0,
                "reward_scale": 0,
            },
            dataset_id="dataset_id",
            finetuned_model="https://example.com",
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            optimizer_config={
                "lr": 0,
                "lr_min": 0,
                "optimizer_type": "adam",
                "weight_decay": 0,
            },
            training_config={
                "batch_size": 0,
                "enable_activation_checkpointing": True,
                "fsdp_cpu_offload": True,
                "memory_efficient_fsdp_wrap": True,
                "n_epochs": 0,
                "n_iters": 0,
                "shuffle": True,
            },
            validation_dataset_id="validation_dataset_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @parametrize
    async def test_raw_response_preference_optimize(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.post_training.with_raw_response.preference_optimize(
            algorithm="dpo",
            algorithm_config={
                "epsilon": 0,
                "gamma": 0,
                "reward_clip": 0,
                "reward_scale": 0,
            },
            dataset_id="dataset_id",
            finetuned_model="https://example.com",
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            optimizer_config={
                "lr": 0,
                "lr_min": 0,
                "optimizer_type": "adam",
                "weight_decay": 0,
            },
            training_config={
                "batch_size": 0,
                "enable_activation_checkpointing": True,
                "fsdp_cpu_offload": True,
                "memory_efficient_fsdp_wrap": True,
                "n_epochs": 0,
                "n_iters": 0,
                "shuffle": True,
            },
            validation_dataset_id="validation_dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post_training = await response.parse()
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @parametrize
    async def test_streaming_response_preference_optimize(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.post_training.with_streaming_response.preference_optimize(
            algorithm="dpo",
            algorithm_config={
                "epsilon": 0,
                "gamma": 0,
                "reward_clip": 0,
                "reward_scale": 0,
            },
            dataset_id="dataset_id",
            finetuned_model="https://example.com",
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            optimizer_config={
                "lr": 0,
                "lr_min": 0,
                "optimizer_type": "adam",
                "weight_decay": 0,
            },
            training_config={
                "batch_size": 0,
                "enable_activation_checkpointing": True,
                "fsdp_cpu_offload": True,
                "memory_efficient_fsdp_wrap": True,
                "n_epochs": 0,
                "n_iters": 0,
                "shuffle": True,
            },
            validation_dataset_id="validation_dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post_training = await response.parse()
            assert_matches_type(PostTrainingJob, post_training, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_supervised_fine_tune(self, async_client: AsyncLlamaStackClient) -> None:
        post_training = await async_client.post_training.supervised_fine_tune(
            algorithm="full",
            algorithm_config={
                "alpha": 0,
                "apply_lora_to_mlp": True,
                "apply_lora_to_output": True,
                "lora_attn_modules": ["string"],
                "rank": 0,
            },
            dataset_id="dataset_id",
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            model="model",
            optimizer_config={
                "lr": 0,
                "lr_min": 0,
                "optimizer_type": "adam",
                "weight_decay": 0,
            },
            training_config={
                "batch_size": 0,
                "enable_activation_checkpointing": True,
                "fsdp_cpu_offload": True,
                "memory_efficient_fsdp_wrap": True,
                "n_epochs": 0,
                "n_iters": 0,
                "shuffle": True,
            },
            validation_dataset_id="validation_dataset_id",
        )
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @parametrize
    async def test_method_supervised_fine_tune_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        post_training = await async_client.post_training.supervised_fine_tune(
            algorithm="full",
            algorithm_config={
                "alpha": 0,
                "apply_lora_to_mlp": True,
                "apply_lora_to_output": True,
                "lora_attn_modules": ["string"],
                "rank": 0,
            },
            dataset_id="dataset_id",
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            model="model",
            optimizer_config={
                "lr": 0,
                "lr_min": 0,
                "optimizer_type": "adam",
                "weight_decay": 0,
            },
            training_config={
                "batch_size": 0,
                "enable_activation_checkpointing": True,
                "fsdp_cpu_offload": True,
                "memory_efficient_fsdp_wrap": True,
                "n_epochs": 0,
                "n_iters": 0,
                "shuffle": True,
            },
            validation_dataset_id="validation_dataset_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @parametrize
    async def test_raw_response_supervised_fine_tune(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.post_training.with_raw_response.supervised_fine_tune(
            algorithm="full",
            algorithm_config={
                "alpha": 0,
                "apply_lora_to_mlp": True,
                "apply_lora_to_output": True,
                "lora_attn_modules": ["string"],
                "rank": 0,
            },
            dataset_id="dataset_id",
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            model="model",
            optimizer_config={
                "lr": 0,
                "lr_min": 0,
                "optimizer_type": "adam",
                "weight_decay": 0,
            },
            training_config={
                "batch_size": 0,
                "enable_activation_checkpointing": True,
                "fsdp_cpu_offload": True,
                "memory_efficient_fsdp_wrap": True,
                "n_epochs": 0,
                "n_iters": 0,
                "shuffle": True,
            },
            validation_dataset_id="validation_dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post_training = await response.parse()
        assert_matches_type(PostTrainingJob, post_training, path=["response"])

    @parametrize
    async def test_streaming_response_supervised_fine_tune(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.post_training.with_streaming_response.supervised_fine_tune(
            algorithm="full",
            algorithm_config={
                "alpha": 0,
                "apply_lora_to_mlp": True,
                "apply_lora_to_output": True,
                "lora_attn_modules": ["string"],
                "rank": 0,
            },
            dataset_id="dataset_id",
            hyperparam_search_config={"foo": True},
            job_uuid="job_uuid",
            logger_config={"foo": True},
            model="model",
            optimizer_config={
                "lr": 0,
                "lr_min": 0,
                "optimizer_type": "adam",
                "weight_decay": 0,
            },
            training_config={
                "batch_size": 0,
                "enable_activation_checkpointing": True,
                "fsdp_cpu_offload": True,
                "memory_efficient_fsdp_wrap": True,
                "n_epochs": 0,
                "n_iters": 0,
                "shuffle": True,
            },
            validation_dataset_id="validation_dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post_training = await response.parse()
            assert_matches_type(PostTrainingJob, post_training, path=["response"])

        assert cast(Any, response.is_closed) is True
