#!/bin/bash

# Nome do ambiente virtual (substitua por um nome adequado)
VIRTUAL_ENV=llm-zoomcamp

# Verifica se o ambiente já existe e o remove se necessário
if [ -d "$VIRTUAL_ENV" ]; then
  echo "O ambiente virtual '$VIRTUAL_ENV' já existe. Removendo..."
  rm -rf "$VIRTUAL_ENV"
fi

# Cria o ambiente virtual
python3 -m venv "$VIRTUAL_ENV"

# Ativa o ambiente virtual
source "$VIRTUAL_ENV/bin/activate"

# Caminho para o site-packages (ajuste conforme necessário)
SITE_PACKAGES="$VIRTUAL_ENV/lib/python3.8/site-packages"

# Instalar as bibliotecas
pip install --target="$SITE_PACKAGES" -r ./requirements.txt --upgrade

# # Desativa o ambiente virtual (opcional, caso queira sair do ambiente)
# deactivate

echo "Ambiente virtual '$VIRTUAL_ENV' criado e dependências instaladas com sucesso!"