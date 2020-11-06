#!/bin/bash
set -ex

mypy --check-untyped-defs scaffold tests
python -m unittest
