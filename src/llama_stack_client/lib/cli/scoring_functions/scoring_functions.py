# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import click

from .list import list_scoring_functions


@click.group()
def scoring_functions():
    """Manage scoring functions"""
    pass


# Register subcommands
scoring_functions.add_command(list_scoring_functions)
