from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Dados para a tabela
data = [
    ["Aplicação", "Horusec", "", "", "", "Semgrep", "", "", "Coverity", "", "", "SonarCloud", "", ""],
    ["", "C", "H", "M", "L", "H", "M", "L", "H", "M", "L", "H", "M", "L"],
    ["Jitsi", 214, 44, 6, 8, 1, 29, "--", 3, 40, 22, 0, 10, 18],
    ["Juice Shop", 379, 107, 8, 3, 36, 57, 4, 16, 34, 157, 191, 28, 61],
    ["PhpMyAdmin", 208, 96, "--", "--", 62, 10, "--", 6, 45, 81, 29, 27, 132],
    ["Reaction", 103, 2, 1, 3, 1, 38, "--", 9, 7, 37, 3, 6, 9],
    ["Rocket.Chat", 1170, 258, 25, 15, 19, 280, 16, 43, 898, 272, 34, 190, 156],
    ["Zen Cart", 1227, 39, "--", 1, 750, 1517, "--", 47, 21, 281, 93, 52, 44],
]

# Função para criar o PDF
def create_pdf(filename):
    pdf = SimpleDocTemplate(filename, pagesize=landscape(letter))
    elements = []

    # Criar a tabela
    table = Table(data, colWidths=[80] + [35] * (len(data[0]) - 1))

    # Estilo da tabela
    style = TableStyle([
        # Merge das células de ferramentas no cabeçalho
        ("SPAN", (1, 0), (4, 0)),  # Merge "Horusec"
        ("SPAN", (5, 0), (7, 0)),  # Merge "Semgrep"
        ("SPAN", (8, 0), (10, 0)), # Merge "Coverity"
        ("SPAN", (11, 0), (13, 0)), # Merge "SonarCloud"
        # Grade da tabela
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        # Centralizar texto
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        # Cabeçalhos em negrito e com fundo cinza claro
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, 1), (-1, 1), "Helvetica-Bold"),
        ("BACKGROUND", (1, 0), (4, 0), colors.lightblue),  # Fundo "Horusec"
        ("BACKGROUND", (5, 0), (7, 0), colors.lightgreen),  # Fundo "Semgrep"
        ("BACKGROUND", (8, 0), (10, 0), colors.lightyellow), # Fundo "Coverity"
        ("BACKGROUND", (11, 0), (13, 0), colors.lightpink), # Fundo "SonarCloud"
        ("BACKGROUND", (1, 1), (4, -1), colors.whitesmoke),  # Fundo colunas "Horusec"
        ("BACKGROUND", (5, 1), (7, -1), colors.lightgreen),  # Fundo colunas "Semgrep"
        ("BACKGROUND", (8, 1), (10, -1), colors.lightyellow), # Fundo colunas "Coverity"
        ("BACKGROUND", (11, 1), (13, -1), colors.lightpink), # Fundo colunas "SonarCloud"
        # Texto padrão
        ("FONTSIZE", (0, 0), (-1, -1), 10),
    ])
    table.setStyle(style)

    # Adicionar a tabela ao PDF
    elements.append(table)

    # Construir o PDF
    pdf.build(elements)

# Criar o PDF
create_pdf("tabela_vulnerabilidades_colorida.pdf")