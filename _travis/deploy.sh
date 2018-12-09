#!/bin/bash

set -e
set -x

python -m pip install -U twine
twine --version

python setup.py build $PYPI_BUILD
twine upload dist/* -u $PYPI_USERNAME -p $PYPI_PASSWORD --skip-existing
