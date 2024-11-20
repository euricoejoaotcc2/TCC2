#!/bin/bash

# Diretório contendo os arquivos CSV
DIRECTORY="./"

# Loop para processar todos os arquivos .csv no diretório
for file in "$DIRECTORY"*.csv; do
    if [ -f "$file" ]; then
        echo "Processando arquivo: $file"

        # Contar vulnerabilidades por nível de impacto
        critical=$(awk -F, '$3 ~ /Critical/ {count++} END {print count+0}' "$file")
        high=$(awk -F, '$3 ~ /High/ {count++} END {print count+0}' "$file")
        medium=$(awk -F, '$3 ~ /Medium/ {count++} END {print count+0}' "$file")
        low=$(awk -F, '$3 ~ /Low/ {count++} END {print count+0}' "$file")
        unspecified=$(awk -F, '$3 ~ /Unspecified/ {count++} END {print count+0}' "$file")

        # Exibir os resultados para o arquivo
        echo "Contagem de vulnerabilidades por impacto:"
        echo "  CRITICAL: $critical"
        echo "  HIGH: $high"
        echo "  MEDIUM: $medium"
        echo "  LOW: $low"
        echo "  UNSPECIFIED: $unspecified"
        echo "-------------------------"
    else
        echo "Nenhum arquivo CSV encontrado no diretório."
    fi
done

