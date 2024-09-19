#!/bin/bash

DESKTOP_FILE="youdzer.desktop"
PYTHON_DESTINATION_DIR=""$HOME"/youdzer/"
BASH_DESTINATION_DIR="/usr/local/bin/youdzer/"
ICON_DESTINATION_DIR="/usr/share/icons/youdzer/"
DESKTOP_DESTINATION_DIR=""$HOME"/.local/share/applications/"
SOURCE_DIR="$(dirname "$0")"

echo ""
sleep 1  # Espera meio segundo
sudo rm -rf "$PYTHON_DESTINATION_DIR"
echo ""

sleep 0.5  # Espera meio segundo
sudo rm -rf "$BASH_DESTINATION_DIR"
echo ""

sleep 0.5  # Espera meio segundo
sudo rm -rf "$ICON_DESTINATION_DIR"
echo ""

sleep 0.5  # Espera meio segundo
sudo rm "$DESKTOP_DESTINATION_DIR""$DESKTOP_FILE"
echo ""

echo ""