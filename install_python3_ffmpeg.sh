#!/bin/bash

# Função para verificar se o Python 3 está instalado
check_python() {
    # Verifica se o Python 3 está instalado
    if ! command -v python3 &> /dev/null; then
        echo "Python 3 não está instalado. Instalando..."
        sudo apt install -y python3 python3-pip python3-venv
    else
        echo "Python 3 já está instalado."
    fi

    # Verifica se o pip3 está instalado
    if ! command -v pip3 &> /dev/null; then
        echo "Python 3 pip não está instalado. Instalando..."
        sudo apt install -y python3-pip
    else
        echo "pip já está instalado."
    fi

    # Verifica se o venv está instalado
    if ! dpkg -l | grep -q "python3-venv"; then
        echo "Python 3 venv não está instalado. Instalando..."
        sudo apt install -y python3-venv
    else
        echo "venv já está instalado."
    fi

    # Verifica se o ffmpeg está instalado
    if ! command -v ffmpeg &> /dev/null; then
        echo "ffmpeg não está instalado. Instalando..."
        sudo apt install -y ffmpeg
    else
        echo "ffmpeg já está instalado."
    fi
}

echo "Verificando se o Python 3 e suas dependências estão instalados. Se não estiverem, a instalação será iniciada..."
sleep 1  # Espera 1 segundo
check_python