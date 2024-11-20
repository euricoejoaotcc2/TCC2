#!/bin/bash

DIRECTORY="./"

for file in "$DIRECTORY"*.json; do
    if [ -f "$file" ]; then
        echo "Processing file: $file"

        critical=$(jq '.analysisVulnerabilities[].vulnerabilities.severity' "$file" | grep -c "CRITICAL")
        high=$(jq '.analysisVulnerabilities[].vulnerabilities.severity' "$file" | grep -c "HIGH")
        medium=$(jq '.analysisVulnerabilities[].vulnerabilities.severity' "$file" | grep -c "MEDIUM")
        low=$(jq '.analysisVulnerabilities[].vulnerabilities.severity' "$file" | grep -c "LOW")
        info=$(jq '.analysisVulnerabilities[].vulnerabilities.severity' "$file" | grep -c "INFO")

        echo "Vulnerability counts:"
        echo "  CRITICAL: $critical"
        echo "  HIGH: $high"
        echo "  MEDIUM: $medium"
        echo "  LOW: $low"
        echo "  INFO: $info"
        echo "-------------------------"
    else
        echo "Sem arquivos JSON no diretório"
    fi
done

