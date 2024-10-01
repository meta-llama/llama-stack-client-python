# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.
import yaml
from llama_stack_client.lib.cli.constants import LLAMA_STACK_CLIENT_CONFIG_DIR


class Subcommand:
    """All llama cli subcommands must inherit from this class"""

    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def create(cls, *args, **kwargs):
        return cls(*args, **kwargs)

    def _add_arguments(self):
        pass
