#!/bin/bash
set -ex

mypy --check-untyped-defs scaffold tests
pytest -s --hypothesis-show-statistics