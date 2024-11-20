import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

# Lista dos arquivos e suas respectivas aplicações
files = {
    "Jitsi Meet": "./jitsi-meet.csv",
    "OWASP Juice Shop": "./owasp-juice-shop.csv",
    "PhpMyAdmin": "./php-my-admin.csv",
    "Reaction": "./reaction.csv",
    "Rocket.Chat": "./rocket-chat.csv",
    "Zen Cart": "./zen-cart.csv",
}

# Função para criar gráficos com paleta de cores e ordenação decrescente
def create_bar_charts_with_ordered_values(files):
    for app_name, file_path in files.items():
        try:
            # Carregar o CSV e ajustar os nomes das colunas
            df = pd.read_csv(file_path)
            df.columns = df.columns.str.strip()  # Remover espaços extras

            # Verificar se as colunas necessárias estão presentes
            if 'ferramenta_utilizada' in df.columns and 'security_total' in df.columns:
                # Agrupar e somar os valores por ferramenta, ordenando de forma decrescente
                grouped_data = df.groupby('ferramenta_utilizada')['security_total'].sum()
                grouped_data = grouped_data.sort_values(ascending=False)

                values = grouped_data.values

                # Criar uma paleta de cores baseada nos valores
                norm = plt.Normalize(values.min(), values.max())
                colors = cm.Blues(norm(values))  # Usar a paleta "Blues"

                # Criar o gráfico de barras
                fig, ax = plt.subplots(figsize=(8, 6))
                bars = ax.bar(grouped_data.index, grouped_data.values, color=colors, edgecolor='black')

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
                cbar.set_label("Security hotspots (intensidade)")

                # Personalizar o gráfico
                ax.set_title(f"Security hotspots por ferramenta utilizada ({app_name})", fontsize=14)
                ax.set_ylabel("Security hotspots", fontsize=12)
                ax.set_xlabel("Ferramenta utilizada", fontsize=12)
                ax.set_xticks(range(len(grouped_data.index)))
                ax.set_xticklabels(grouped_data.index, rotation=45, ha="right", fontsize=10)
                plt.tight_layout()

                # Salvar o gráfico como PDF
                plt.savefig(f"{app_name.replace(' ', '_').lower()}_grafico.pdf", format="pdf", dpi=300)
                plt.close()  # Fechar para evitar sobreposição
            else:
                print(f"As colunas necessárias estão ausentes no CSV da aplicação {app_name}.")
        except Exception as e:
            print(f"Erro ao processar o arquivo {app_name}: {e}")

# Gerar os gráficos
create_bar_charts_with_ordered_values(files)