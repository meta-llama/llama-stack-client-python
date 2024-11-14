# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from typing import Optional

import click

# from rich.console import Console
# from rich.table import Table
from tqdm.rich import tqdm


@click.command("run_benchmark")
@click.option("--eval-task-id", required=True, help="ID of the eval task")
@click.option(
    "--num-examples", required=False, help="Number of examples to evaluate on, useful for debugging", default=None
)
@click.pass_context
def run_benchmark(ctx, eval_task_id: str, num_examples: Optional[int]):
    """Run a evaluation benchmark"""

    client = ctx.obj["client"]

    eval_task = client.eval_tasks.retrieve(name=eval_task_id)
    scoring_functions = eval_task.scoring_functions
    dataset_id = eval_task.dataset_id

    rows = client.datasetio.get_rows_paginated(
        dataset_id=dataset_id, rows_in_page=-1 if num_examples is None else num_examples
    )

    for row in rows:
        print(row)

    output_res = {
        "chat_completion_input": [],
        "generated_output": [],
        "expected_output": [],
    }
    for x in scoring_functions:
        output_res[x] = []

    for r in tqdm(rows.rows):
        eval_res = client.eval.evaluate_rows(
            task_id=eval_task_id,
            input_rows=[r],
            scoring_functions=scoring_functions,
            task_config={
                "type": "benchmark",
                "eval_candidate": {
                    "type": "model",
                    "model": "Llama3.2-3B-Instruct",
                    "sampling_params": {
                        "strategy": "greedy",
                        "temperature": 0,
                        "top_p": 0.95,
                        "top_k": 0,
                        "max_tokens": 0,
                        "repetition_penalty": 1.0,
                    },
                },
            },
        )
    # if eval_tasks_list_response:
    #     table = Table()
    #     for header in headers:
    #         table.add_column(header)

    #     for item in eval_tasks_list_response:
    #         table.add_row(*[str(getattr(item, header)) for header in headers])
    #     console.print(table)
