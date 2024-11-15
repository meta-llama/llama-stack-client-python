# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.


import click

from .run_benchmark import run_benchmark
from .run_scoring import run_scoring


@click.group()
def eval():
    """Run evaluation tasks"""
    pass


# Register subcommands
eval.add_command(run_benchmark)
eval.add_command(run_scoring)
