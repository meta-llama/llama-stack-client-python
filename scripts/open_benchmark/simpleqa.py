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


async def run_main(
    host: str,
    port: int,
    model_id: str,
    use_https: Optional[bool] = False,
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

    eval_rows = client.datasetio.get_rows_paginated(
        dataset_id="simpleqa",
        rows_in_page=5,
    )

    response = client.eval.evaluate_rows_alpha(
        benchmark_id="meta-reference-simpleqa",
        input_rows=eval_rows.rows,
        scoring_functions=["llm-as-judge::405b-simpleqa"],
        task_config={
            "type": "benchmark",
            "eval_candidate": {
                "type": "model",
                "model": model_id,
                "sampling_params": {
                    "temperature": 0.0,
                    "max_tokens": 4096,
                    "top_p": 0.9,
                    "repeat_penalty": 1.0,
                },
            },
        },
    )

    print(response)


def main(
    host: str,
    port: int,
    model: str,
    use_https: Optional[bool] = False,
    cert_path: Optional[str] = None,
):
    asyncio.run(
        run_main(
            host,
            port,
            model,
            use_https,
            cert_path,
        )
    )


if __name__ == "__main__":
    fire.Fire(main)
