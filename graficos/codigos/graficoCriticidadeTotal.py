import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Substituir pelo caminho correto do seu CSV
file_path = "../csvs/criticidade.csv"
df = pd.read_csv(file_path)

# Substituir valores ausentes ou '--' por 0
df.replace("--", 0, inplace=True)
df.fillna(0, inplace=True)

# Cores das categorias
colors = {
    "Critical": "orange",
    "High": "red",
    "Medium": "yellow",
    "Low": "blue"
}

# Dados reorganizados para o gráfico
categories = ["Critical", "High", "Medium", "Low"]
tools = ["Horusec", "Semgrep", "Coverity", "SonarCloud"]

# Configuração do gráfico
plt.figure(figsize=(14, 8))
bar_width = 0.2
y_positions = np.arange(len(tools))

# Plotar cada categoria e adicionar valores
for i, category in enumerate(categories):
    if category == "Critical":  # Excluir Critical para ferramentas que não possuem esta categoria
        values = [df[f"{tool}_C"].sum() if tool == "Horusec" else 0 for tool in tools]
    else:
        values = [
            df[f"{tool}_{category[0]}"].sum() for tool in tools
        ]  # Pega os valores de High, Medium e Low

    # Verificar se há valores diferentes de 0 antes de plotar
    if any(values):
        bars = plt.barh(
            y_positions + i * bar_width, values, height=bar_width,
            label=category, color=colors[category]
        )
        # Adicionar os valores inteiros sobre as barras
        for bar, value in zip(bars, values):
            if value > 0:  # Exibir apenas valores maiores que 0
                plt.text(
                    bar.get_width() + 5,  # Posição x
                    bar.get_y() + bar.get_height() / 2,  # Posição y
                    str(int(value)),  # Valor a ser exibido
                    va='center', ha='left', fontsize=10
                )

# Configurar o gráfico
plt.yticks(y_positions + bar_width * 1.5, tools)
plt.xlabel("Quantidade de Vulnerabilidades")
plt.title("Total de vulnerabilidades por Ferramenta e Categoria")
plt.legend(title="Categorias", bbox_to_anchor=(1.05, 1), loc='upper left')

# Salvar o gráfico como PDF
plt.tight_layout()
plt.savefig("grafico_vulnerabilidades_horizontal_sem_critical_zeros.pdf")
