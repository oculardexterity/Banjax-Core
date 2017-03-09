#!/bin/bash 
virtualenv -p python3 venv
source venv/bin/activate
pip install --upgrade pip

pip install -r requirements/common.txt
pip install -r requirements/dev.txt

echo "\n\n\n\n"
echo "(hey Bilu... I'm installing shit on you computer)"
echo 'Now run: \n source venv/bin/activate \n\n and then: \n\n python app.py'