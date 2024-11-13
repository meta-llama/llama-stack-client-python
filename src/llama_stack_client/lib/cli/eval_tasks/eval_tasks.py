# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.


import click

from .list import list_eval_tasks


@click.group()
def eval_tasks():
    """Query details about available eval tasks type on distribution."""
    pass


# Register subcommands
eval_tasks.add_command(list_eval_tasks)
