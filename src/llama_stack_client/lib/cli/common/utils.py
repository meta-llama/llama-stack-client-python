# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.
from rich.console import Console
from rich.table import Table


def create_bar_chart(data, labels, title=""):
    """Create a bar chart using Rich Table."""

    console = Console()
    table = Table(title=title)
    table.add_column("Score")
    table.add_column("Count")

    max_value = max(data)
    total_count = sum(data)

    # Define a list of colors to cycle through
    colors = ["green", "blue", "red", "yellow", "magenta", "cyan"]

    for i, (label, value) in enumerate(zip(labels, data)):
        bar_length = int((value / max_value) * 20)  # Adjust bar length as needed
        bar = "█" * bar_length + " " * (20 - bar_length)
        color = colors[i % len(colors)]
        table.add_row(label, f"[{color}]{bar}[/] {value}/{total_count}")

    console.print(table)
