# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import click

from .list import list_shields


@click.group()
def shields():
    """Query details about available safety shields on distribution."""
    pass


# Register subcommands
shields.add_command(list_shields)
