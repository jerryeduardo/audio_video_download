#!/bin/bash

# Define o caminho do arquivo .desktop e o diretório de destino
DESKTOP_FILE="youdzer.desktop"
DESTINATION_DIR="/usr/share/applications/"

sudo cp "$DESKTOP_FILE" "$DESTINATION_DIR"