#! /bin/bash
virtualenv venv --python=`which python3` --prompt="(mt940)" --clear
source venv/bin/activate
pip install --upgrade pip
pip install --upgrade wheel
