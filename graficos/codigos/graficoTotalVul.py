import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

# Lista dos arquivos e suas respectivas aplicações
files = {
    "Jitsi Meet": "../csvs/jitsi-meet.csv",
    "OWASP Juice Shop": "../csvs/owasp-juice-shop.csv",
    "PhpMyAdmin": "../csvs/php-my-admin.csv",
    "Reaction": "../csvs/reaction.csv",
    "Rocket.Chat": "../csvs/rocket-chat.csv",
    "Zen Cart": "../csvs/zen-cart.csv",
}

# Criar um gráfico consolidado com o total de vulnerabilidades por ferramenta utilizando todos os CSVs
def create_consolidated_chart(files):
    try:
        # DataFrame para consolidar os dados de todos os arquivos
        consolidated_data = pd.DataFrame()

        # Processar cada arquivo e somar as vulnerabilidades por ferramenta
        for app_name, file_path in files.items():
            df = pd.read_csv(file_path)
            df.columns = df.columns.str.strip()  # Remover espaços extras
            if 'ferramenta_utilizada' in df.columns and 'security_total' in df.columns:
                # Agrupar e somar os valores por ferramenta
                grouped_data = df.groupby('ferramenta_utilizada')['security_total'].sum()
                consolidated_data = pd.concat([consolidated_data, grouped_data], axis=1)
            else:
                print(f"As colunas necessárias estão ausentes no CSV da aplicação {app_name}.")

        # Consolidar os dados somando os valores para cada ferramenta
        consolidated_data['total'] = consolidated_data.sum(axis=1)

        # Ordenar os dados por total de vulnerabilidades
        consolidated_data = consolidated_data[['total']].sort_values(by='total', ascending=False)

        # Criar uma paleta de cores baseada nos valores
        values = consolidated_data['total'].values
        norm = plt.Normalize(values.min(), values.max())
        colors = cm.Blues(norm(values))

        # Criar o gráfico de barras
        fig, ax = plt.subplots(figsize=(10, 7))
        bars = ax.bar(consolidated_data.index, consolidated_data['total'], color=colors, edgecolor='black')

        # Adicionar os números nas barras
        for bar in bars:
            height = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2,  # Posição X
                height,  # Posição Y
                f'{int(height)}',  # Valor do texto
                ha='center', va='bottom', fontsize=10  # Alinhamento e tamanho da fonte
            )

        # Adicionar barra de cores associada ao gráfico
        cbar = fig.colorbar(cm.ScalarMappable(norm=norm, cmap="Blues"), ax=ax, pad=0.02)
        cbar.set_label("Vulnerabilidades de segurança (intensidade)")

        # Personalizar o gráfico
        ax.set_title("Total de vulnerabilidades por ferramenta", fontsize=16)
        ax.set_ylabel("Total de vulnerabilidades", fontsize=12)
        ax.set_xlabel("Ferramenta utilizada", fontsize=12)
        ax.set_xticks(range(len(consolidated_data.index)))
        ax.set_xticklabels(consolidated_data.index, rotation=45, ha="right", fontsize=10)
        plt.tight_layout()

        # Salvar o gráfico como PDF
        plt.savefig("total_vulnerabilidades_por_ferramenta.pdf", format="pdf", dpi=300)
        plt.close()

        print("Gráfico consolidado salvo como 'total_vulnerabilidades_por_ferramenta.pdf'.")
    except Exception as e:
        print(f"Erro ao criar o gráfico consolidado: {e}")

# Criar o gráfico consolidado
create_consolidated_chart(files)
