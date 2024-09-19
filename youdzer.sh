#!/bin/bash

# Define o nome da pasta do usuário e o nome do ambiente virtual do python
PYTHON_DESTINATION_DIR=""$HOME"/youdzer/"
VIRTUAL_ENV="yd-env/bin/activate"

source "$PYTHON_DESTINATION_DIR""$VIRTUAL_ENV"
python "$PYTHON_DESTINATION_DIR"index.py