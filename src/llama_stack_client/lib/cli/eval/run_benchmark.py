# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import json
import os
from typing import Optional

import click
from rich import print as rprint
from tqdm.rich import tqdm

from ..common.utils import create_bar_chart


@click.command("run-benchmark")
@click.argument("eval-task-ids", nargs=-1, required=True)
@click.option(
    "--eval-task-config",
    required=True,
    help="Path to the eval task config file in JSON format",
    type=click.Path(exists=True),
)
@click.option(
    "--output-dir",
    required=True,
    help="Path to the dump eval results output directory",
)
@click.option(
    "--num-examples",
    required=False,
    help="Number of examples to evaluate on, useful for debugging",
    default=None,
    type=int,
)
@click.option(
    "--visualize",
    is_flag=True,
    default=False,
    help="Visualize evaluation results after completion",
)
@click.pass_context
def run_benchmark(
    ctx,
    eval_task_ids: tuple[str, ...],
    eval_task_config: str,
    output_dir: str,
    num_examples: Optional[int],
    visualize: bool,
):
    """Run a evaluation benchmark task"""

    client = ctx.obj["client"]

    for eval_task_id in eval_task_ids:
        eval_task = client.eval_tasks.retrieve(name=eval_task_id)
        scoring_functions = eval_task.scoring_functions
        dataset_id = eval_task.dataset_id

        rows = client.datasetio.get_rows_paginated(
            dataset_id=dataset_id, rows_in_page=-1 if num_examples is None else num_examples
        )

        with open(eval_task_config, "r") as f:
            eval_task_config = json.load(f)

        output_res = {}

        for r in tqdm(rows.rows):
            eval_res = client.eval.evaluate_rows(
                task_id=eval_task_id,
                input_rows=[r],
                scoring_functions=scoring_functions,
                task_config=eval_task_config,
            )
            for k in r.keys():
                if k not in output_res:
                    output_res[k] = []
                output_res[k].append(r[k])

            for k in eval_res.generations[0].keys():
                if k not in output_res:
                    output_res[k] = []
                output_res[k].append(eval_res.generations[0][k])

            for scoring_fn in scoring_functions:
                if scoring_fn not in output_res:
                    output_res[scoring_fn] = []
                output_res[scoring_fn].append(eval_res.scores[scoring_fn].score_rows[0])

        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        # Save results to JSON file
        output_file = os.path.join(output_dir, f"{eval_task_id}_results.json")
        with open(output_file, "w") as f:
            json.dump(output_res, f, indent=2)

        rprint(f"[green]✓[/green] Results saved to: [blue]{output_file}[/blue]!\n")

        if visualize:
            for scoring_fn in scoring_functions:
                res = output_res[scoring_fn]
                assert len(res) > 0 and "score" in res[0]
                scores = [str(r["score"]) for r in res]
                unique_scores = sorted(list(set(scores)))
                counts = [scores.count(s) for s in unique_scores]
                create_bar_chart(counts, unique_scores, title=f"{scoring_fn}")
