# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import json
import os
from typing import Optional

import click
import pandas
from rich import print as rprint
from tqdm.rich import tqdm


@click.command("run_scoring")
@click.argument("scoring-function-ids", nargs=-1, required=True)
@click.option(
    "--dataset-id",
    required=True,
    help="Pre-registered dataset_id to score (from llama-stack-client datasets list)",
)
@click.option(
    "--scoring-params-config",
    required=False,
    help="Path to the scoring params config file in JSON format",
    type=click.Path(exists=True),
)
@click.option(
    "--output-dir",
    required=True,
    help="Path to the dump eval results output directory",
)
@click.option(
    "--visualize",
    is_flag=True,
    default=False,
    help="Visualize evaluation results after completion",
)
@click.pass_context
def run_scoring(
    ctx,
    scoring_function_ids: tuple[str, ...],
    dataset_id: str,
    scoring_params_config: Optional[str],
    output_dir: str,
    visualize: bool,
):
    """Run scoring from application datasets"""
    client = ctx.obj["client"]

    scoring_params = {fn_id: None for fn_id in scoring_function_ids}
    if scoring_params_config:
        with open(scoring_params_config, "r") as f:
            scoring_params = json.load(f)
            print(scoring_params)

    dataset = client.datasets.retrieve(dataset_id=dataset_id)
    if not dataset:
        click.BadParameter(
            f"Dataset {dataset_id} not found. Please register using llama-stack-client datasets register"
        )

    output_res = {}

    rows = client.datasetio.get_rows_paginated(dataset_id=dataset_id, rows_in_page=-1)
    for r in tqdm(rows.rows):
        score_res = client.scoring.score(
            input_rows=[r],
            scoring_functions=scoring_params,
        )
        for k in r.keys():
            if k not in output_res:
                output_res[k] = []
            output_res[k].append(r[k])

        for fn_id in scoring_function_ids:
            if fn_id not in output_res:
                output_res[fn_id] = []
            output_res[fn_id].append(score_res.results[fn_id].score_rows[0])

        break

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"{dataset_id}_score_results.csv")
    df = pandas.DataFrame(output_res)
    df.to_csv(output_file, index=False)

    rprint(f"[green]✓[/green] Results saved to: [blue]{output_file}[/blue]!\n")
