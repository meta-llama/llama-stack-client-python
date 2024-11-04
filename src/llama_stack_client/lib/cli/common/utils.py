# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.
from tabulate import tabulate


def print_table_from_response(response, headers=()):
    if not headers:
        headers = sorted(response[0].__dict__.keys())

    rows = []
    for spec in response:
        rows.append([spec.__dict__[headers[i]] for i in range(len(headers))])

    print(tabulate(rows, headers=headers, tablefmt="grid"))
