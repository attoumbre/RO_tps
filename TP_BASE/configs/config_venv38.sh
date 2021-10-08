#!/usr/bin/env bash

# USAGE:
#   ./configs/config_venv38.sh

python3.8 -m pip install --upgrade pip
python3.8 -m pip install virtualenv
python3.8 -m virtualenv .venv_38
source ./.venv_38/bin/activate
pip install wheel # necessary to install with bdist_wheel
pip install -r requirements/requirements.txt
