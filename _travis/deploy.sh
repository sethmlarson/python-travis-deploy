#!/bin/bash

set -e
set -x

python -m pip install -U twine setuptools wheel
twine --version

python setup.py build bdist_wheel
if [ "$TOXENV" = "py36" ]; then
  python setup.py build sdist
fi

twine upload dist/* -u $PYPI_USERNAME -p $PYPI_PASSWORD --skip-existing
