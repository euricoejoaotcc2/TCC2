import pandas as pd
import matplotlib.pyplot as plt
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

# Criar gráfico agrupado para todas as aplicações com subgrupos ordenados
def create_grouped_horizontal_bar_chart_with_custom_colors(files):
    try:
        # DataFrame para consolidar os dados de todas as aplicações
        consolidated_data = {}

        # Processar cada arquivo e consolidar os valores por aplicação e ferramenta
        for app_name, file_path in files.items():
            df = pd.read_csv(file_path)
            df.columns = df.columns.str.strip()  # Remover espaços extras
            if 'ferramenta_utilizada' in df.columns and 'security_total' in df.columns:
                grouped_data = df.groupby('ferramenta_utilizada')['security_total'].sum()
                consolidated_data[app_name] = grouped_data.sort_values(ascending=False)  # Ordenar por valor decrescente
            else:
                print(f"As colunas necessárias estão ausentes no CSV da aplicação {app_name}.")

        # Criar DataFrame consolidado para todas as aplicações
        consolidated_df = pd.DataFrame(consolidated_data).fillna(0)

        # Configurações de cores específicas
        predefined_colors = ['red', 'blue', 'green', 'yellow']
        unique_tools = consolidated_df.index.tolist()
        colors = {tool: predefined_colors[i % len(predefined_colors)] for i, tool in enumerate(unique_tools)}

        # Criar gráfico de barras horizontais agrupadas
        fig, ax = plt.subplots(figsize=(12, 10))
        y = np.arange(len(consolidated_df.columns))  # Posições no eixo Y
        bar_height = 0.15  # Altura das barras

        for i, app in enumerate(consolidated_df.columns):
            app_data = consolidated_df[app].sort_values(ascending=False)  # Ordenar subgrupo
            bars = ax.barh(
                y[i] + np.arange(len(app_data)) * bar_height - (len(app_data) * bar_height / 2),  # Ajustar posição das barras
                app_data.values,
                height=bar_height,
                label=app,
                color=[colors[tool] for tool in app_data.index],  # Atribuir cores específicas
                edgecolor='black'
            )
            # Adicionar os valores exatos ao lado de cada barra
            for bar, tool in zip(bars, app_data.index):
                width = bar.get_width()
                if width > 0:  # Mostrar apenas se houver valor
                    ax.text(
                        width + 5,  # Posição X
                        bar.get_y() + bar.get_height() / 2,  # Posição Y
                        f'{int(width)}',  # Valor do texto
                        va='center', ha='left', fontsize=12, weight='bold'  # Aumentar fonte e deixar em negrito
                    )

        # Personalizar o gráfico
        ax.set_title("Total de Vulnerabilidades por Ferramenta e Aplicação", fontsize=16, weight='bold')
        ax.set_xlabel("Total de Vulnerabilidades", fontsize=14, weight='bold')
        ax.set_ylabel("Aplicações", fontsize=14, weight='bold')
        ax.set_yticks(y)
        ax.set_yticklabels(consolidated_df.columns, fontsize=12, weight='bold')

        # Criar legenda com cores das ferramentas
        legend_handles = [plt.Rectangle((0, 0), 1, 1, color=colors[tool]) for tool in unique_tools]
        legend = ax.legend(legend_handles, unique_tools, title="Ferramentas", fontsize=12, title_fontsize=14, loc="lower right")
        plt.setp(legend.get_texts(), weight='bold')  # Deixar os textos da legenda em negrito

        plt.tight_layout()

        # Salvar o gráfico como PDF
        plt.savefig("vulnerabilidades_agrupadas_horizontal_cores_personalizadas_legenda_ajustada.pdf", format="pdf", dpi=300)
        plt.close()

        print("Gráfico agrupado salvo como 'vulnerabilidades_agrupadas_horizontal_cores_personalizadas_legenda_ajustada.pdf'.")
    except Exception as e:
        print(f"Erro ao criar o gráfico agrupado: {e}")

# Criar o gráfico agrupado com cores personalizadas
create_grouped_horizontal_bar_chart_with_custom_colors(files)
