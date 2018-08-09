#!/bin/bash

clear
echo "Setting up Survivor Support!"

echo "Installing System Dependencies ..."
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

echo "Setting Up Local Environment ..."
export PYTHON_VERSION=`cat runtime.txt | sed -e 's/python-//'`
pyenv install $PYTHON_VERSION -s -v # this takes a little longer than the other steps
pyenv local $PYTHON_VERSION
python -m venv .venv
source .venv/bin/activate 
sudo service postgresql start
make dev-setup

echo "Last step ..."
exec bash -l