import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Exemplo de dados (substitua pela leitura do seu CSV)
# df = pd.read_csv('falsoPositivoReaction.csv', sep=',')
data = {
    'nome_ferramenta': ['Horusec', 'SonarCloud', 'Coverity', 'Semgrep'],
    'qtd_falsoPositivo': [103, 7, 10, 1],
    'total_vulnerabilidades': [109, 18, 53, 39]
}
df = pd.DataFrame(data)

# Cria coluna de porcentagem (qtd_falsoPositivo / total_vulnerabilidades)
df['porcentagem_fp'] = (df['qtd_falsoPositivo'] / df['total_vulnerabilidades']) * 100

# Ordena do maior para o menor em função da porcentagem de falsos positivos
df = df.sort_values('porcentagem_fp', ascending=False).reset_index(drop=True)

# Normalizando valores para aplicar o degradê de cores
norm = plt.Normalize(df['porcentagem_fp'].min(), df['porcentagem_fp'].max())
colors = plt.cm.Reds(norm(df['porcentagem_fp']))

# Criação do gráfico
plt.figure(figsize=(10, 6))
bars = plt.bar(df['nome_ferramenta'], df['qtd_falsoPositivo'], color=colors)

# Título e rótulos dos eixos
plt.title('Análise de falsos positivos da aplicação Reaction Commerce', fontsize=16)
plt.xlabel('Ferramenta', fontsize=14)
plt.ylabel('Quantidade de falsos positivos', fontsize=14)

# Adicionar valores (FP / total, e %)
max_val = df['qtd_falsoPositivo'].max()

for i, bar in enumerate(bars):
    qtd_fp = bar.get_height()  # Falsos positivos (height da barra)
    total_vulns = df.loc[i, 'total_vulnerabilidades']
    porcentagem = df.loc[i, 'porcentagem_fp']
    
    # Rótulo: "x / y" na primeira linha, e "(z%)" na segunda
    label_text = f'{int(qtd_fp)} / {int(total_vulns)}\n({porcentagem:.2f}%)'
    
    # Se a barra for muito alta, escreve dentro (em branco)
    if qtd_fp > 0.6 * max_val:
        plt.text(
            bar.get_x() + bar.get_width()/2,
            qtd_fp / 2,
            label_text,
            ha='center',
            va='center',
            color='white',
            fontsize=12,
            fontweight='bold'
        )
    else:
        # Caso contrário, escreve acima da barra
        plt.text(
            bar.get_x() + bar.get_width()/2,
            qtd_fp + (max_val * 0.01),
            label_text,
            ha='center',
            va='bottom',
            fontsize=12
        )

# Cria uma “legenda” explicando os valores
explicacao_text = (
    "• Falsos positivos / total de vulnerabilidades\n"
    "• (porcentagem de falsos positivos em relação ao total)"
)
explicacao_patch = mpatches.Patch(color='none', label=explicacao_text)
legend = plt.legend(
    handles=[explicacao_patch],
    title="Legenda",
    loc='upper right',
    frameon=True,
    fontsize=11
)

# Ajustes visuais na legenda
legend.set_title("Valores das barras", prop={'size': 13, 'weight': 'bold'})
legend.get_frame().set_edgecolor('black')
legend.get_frame().set_facecolor('white')
legend.get_frame().set_alpha(1)

plt.tight_layout()

# Salva em PDF
plt.savefig("quantidadeDeFalsoPositivo.pdf", format='pdf')
plt.close()
