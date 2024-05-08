#!/bin/bash

if [ ! -d "venv" ]; then
    echo "Creando ambiente virtual..."
    python3 -m venv venv || {
        echo "Error al crear el ambiente virtual."
        exit 1
    }
    echo "Instalando dependencias..."
    source venv/bin/activate || {
        echo "Error al activar el ambiente virtual."
        exit 1
    }
    pip install -r requirements.txt || {
        echo "Error al instalar las dependencias."
        exit 1
    }
fi

echo "Activando ambiente virtual..."
source venv/bin/activate || {
    echo "Error al activar el ambiente virtual."
    exit 1
}

