#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021  Érik Martin-Dorel
#
# Example Python3 program.
#
# Licensed under BSD-3 <https://opensource.org/licenses/BSD-3-Clause>
#
# Report bugs on <https://github.com/erikmd/poc-github-ci/issues>

import os
import sys


def get_script_directory():
    """$(cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd) in Python."""
    return os.path.dirname(__file__)


def get_version():
    with open(os.path.join(get_script_directory(), 'VERSION'), 'r') as f:
        version = f.read().strip()
    return version


def operation(a, b):
    """Compute the addition (currently)"""
    return a * b


def test_indent_script():
    assert operation(2, 2) == 4
    # assert operation(3, 3) == 6


def main(argv):
    if (argv == ['--version']):
        print(get_version())
    else:
        print("""
example.py: Example Python3 program

Installation:
  pip install --no-cache-dir -r requirements.txt

Usage:
  ./example.py --version
  pytest example.py
""")


if __name__ == "__main__":
    main(sys.argv[1:])
