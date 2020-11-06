#!/bin/sh
mypy --check-untyped-defs scaffold tests
python -m unittest
