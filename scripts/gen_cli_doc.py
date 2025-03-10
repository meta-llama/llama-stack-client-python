# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import os
from pathlib import Path

import click
from llama_stack_client.lib.cli.llama_stack_client import cli


def generate_markdown_docs(command, parent=None, level=1):
    """Generate markdown documentation for a click command."""
    ctx = click.Context(command, info_name=command.name, parent=parent)

    # Start with the command name as a header
    prefix = "#" * level
    doc = [f"{prefix} 'CLI Reference'\n"]

    # Add command help docstring
    if command.help:
        doc.append(f"{command.help}\n")

    # Add usage
    doc.append("### Usage\n")
    doc.append(f"```\n{command.get_usage(ctx)}\n```\n")

    # Add options if present
    has_options = False
    for param in command.get_params(ctx):
        if isinstance(param, click.Option):
            if not has_options:
                doc.append("### Options\n")
                has_options = True
            opts = ", ".join(param.opts)
            help_text = param.help or ""
            default = f" [default: {param.default}]" if param.default is not None else ""
            doc.append(f"* **{opts}**: {help_text}{default}\n")

    # Add arguments if present
    has_arguments = False
    for param in command.get_params(ctx):
        if isinstance(param, click.Argument):
            if not has_arguments:
                doc.append("### Arguments\n")
                has_arguments = True
            name = param.name.upper()
            doc.append(f"* **{name}**\n")

    # If this is a group with commands, add subcommands
    if isinstance(command, click.Group):
        doc.append("### Commands\n")
        for cmd_name in command.list_commands(ctx):
            cmd = command.get_command(ctx, cmd_name)
            cmd_help = cmd.get_short_help_str() if cmd else ""
            doc.append(f"* **{cmd_name}**: {cmd_help}\n")

        # Add detailed subcommand documentation
        for cmd_name in command.list_commands(ctx):
            cmd = command.get_command(ctx, cmd_name)
            if cmd:
                doc.append("\n")
                doc.extend(generate_markdown_docs(cmd, ctx, level + 1))

    return doc


if __name__ == "__main__":
    # Generate the docs
    markdown_lines = generate_markdown_docs(cli)
    markdown = "\n".join(markdown_lines)

    # Write to file
    file_path = Path(__file__).parent.parent / "docs" / "cli_reference.md"
    with open(file_path, "w") as f:
        f.write(markdown)

    print(f"Documentation generated in {file_path}")
