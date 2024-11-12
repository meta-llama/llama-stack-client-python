# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import argparse
import json

import os
from pathlib import Path

from tqdm import tqdm

from llama_stack_client import LlamaStackClient
from llama_stack_client.lib.cli.configure import get_config
from llama_stack_client.lib.cli.subcommand import Subcommand


class EvalRunBenchmark(Subcommand):
    def __init__(self, subparsers: argparse._SubParsersAction):
        super().__init__()
        self.parser = subparsers.add_parser(
            "run_benchmark",
            prog="llama-stack-client eval run_benchmark",
            description="Run evaluation benchmark tasks.",
            formatter_class=argparse.RawTextHelpFormatter,
        )
        self._add_arguments()
        self.parser.set_defaults(func=self._run_benchmark_cmd)

    def _add_arguments(self):
        self.parser.add_argument(
            "--endpoint",
            type=str,
            help="Llama Stack distribution endpoint",
        )
        self.parser.add_argument(
            "--benchmark-id",
            type=str,
            help="Benchmark Task ID",
        )

    def _run_benchmark_cmd(self, args: argparse.Namespace):
        args.endpoint = get_config().get("endpoint") or args.endpoint

        client = LlamaStackClient(
            base_url=args.endpoint,
            provider_data={
                "fireworks_api_key": os.environ.get("FIREWORKS_API_KEY"),
            },
        )

        eval_tasks_list_response = client.eval_tasks.list()

        # register dataset
        # TODO: move this to files for registering benchmarks
        client.datasets.register(
            dataset_id="mmlu",
            schema={
                "input_query": {
                    "type": "string",
                },
                "expected_answer": {
                    "type": "string",
                },
            },
            url={
                "uri": "https://huggingface.co/datasets/llamastack/evals",
            },
            metadata={
                "path": "llamastack/evals",
                "name": "evals__mmlu__details",
                "split": "train",
            },
            provider_id="huggingface-0",
        )
        # list datasets
        print(client.datasets.list())

        # register model
        client.models.register(
            model_id="Llama3.2-3B-Instruct",
        )

        # register eval task
        task_id = "meta-reference-mmlu"
        scoring_functions = [
            "basic::regex_parser_multiple_choice_answer",
        ]
        client.eval_tasks.register(
            eval_task_id=task_id,
            dataset_id="mmlu",
            scoring_functions=scoring_functions,
        )

        rows = client.datasetio.get_rows_paginated(
            dataset_id="mmlu",
            rows_in_page=-1,
        )

        output_res = {
            "chat_completion_input": [],
            "generated_output": [],
            "expected_output": [],
        }
        for x in scoring_functions:
            output_res[x] = []

        # run evaluate_rows row by row
        # TODO: jobs for background job scheduling
        for r in tqdm(rows.rows):
            eval_response = client.eval.evaluate_rows(
                task_id=task_id,
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
            output_res["chat_completion_input"].append(r["chat_completion_input"])
            output_res["expected_output"].append(r["expected_answer"])
            output_res["generated_output"].append(eval_response.generations[0]["generated_answer"])
            for scoring_fn in scoring_functions:
                output_res[scoring_fn].append(eval_response.scores[scoring_fn].score_rows[0])

        # TODO: specify output file
        save_path = Path(os.path.abspath(__file__)).parent / f"eval-result-{task_id}.json"
        with open(save_path, "w") as f:
            json.dump(output_res, f, indent=4)

        print(f"Eval result saved at {save_path}!")
