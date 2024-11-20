import pandas as pd
import matplotlib.pyplot as plt

# Lista dos arquivos e suas respectivas aplicações
files = {
    "Jitsi Meet": "caminho_para/jitsi-meet.csv",
    "OWASP Juice Shop": "caminho_para/owasp-juice-shop.csv",
    "PhpMyAdmin": "caminho_para/php-my-admin.csv",
    "Reaction": "caminho_para/reaction.csv",
    "Rocket.Chat": "caminho_para/rocket-chat.csv",
    "Zen Cart": "caminho_para/zen-cart.csv",
}

# Função para criar gráficos de barras com números nas barras
def create_bar_charts_with_values(files):
    for app_name, file_path in files.items():
        try:
            # Carregar o CSV e ajustar os nomes das colunas
            df = pd.read_csv(file_path)
            df.columns = df.columns.str.strip()  # Remover espaços extras

            # Verificar se as colunas necessárias estão presentes
            if 'ferramenta_utilizada' in df.columns and 'security_total' in df.columns:
                # Agrupar e somar os valores por ferramenta
                grouped_data = df.groupby('ferramenta_utilizada')['security_total'].sum()

                # Criar o gráfico de barras
                plt.figure(figsize=(8, 6))
                bars = plt.bar(grouped_data.index, grouped_data.values, color='skyblue', edgecolor='black')

                # Adicionar os números nas barras
                for bar in bars:
                    height = bar.get_height()
                    plt.text(
                        bar.get_x() + bar.get_width() / 2,  # Posição X
                        height,  # Posição Y
                        f'{int(height)}',  # Valor do texto
                        ha='center', va='bottom', fontsize=10  # Alinhamento e tamanho da fonte
                    )

                # Personalizar o gráfico
                plt.title(f"Security hotspots por ferramenta utilizada ({app_name})", fontsize=14)
                plt.ylabel("Security hotspots", fontsize=12)
                plt.xlabel("Ferramenta utilizada", fontsize=12)
                plt.xticks(rotation=45, ha="right", fontsize=10)
                plt.tight_layout()

                # Exibir o gráfico
                plt.show()
            else:
                print(f"As colunas necessárias estão ausentes no CSV da aplicação {app_name}.")
        except Exception as e:
            print(f"Erro ao processar o arquivo {app_name}: {e}")

# Gerar os gráficos
create_bar_charts_with_values(files)
