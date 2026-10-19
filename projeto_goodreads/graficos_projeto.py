"""Estilo comum dos gráficos do projeto Goodreads (matplotlib).

Cores: duas posições fixas de uma paleta categórica validada para daltonismo
(azul para autoria feminina, laranja para autoria masculina). A cor segue o
grupo, nunca a ordem. Todo gráfico tem título, eixos com unidade, legenda ou
rótulo direto e uma tabela equivalente no notebook.
"""

from pathlib import Path

import matplotlib.pyplot as plt

CORES = {"feminino": "#2a78d6", "masculino": "#eb6834"}
NEUTRA = "#52514e"
FUNDO = "#fcfcfb"
TEXTO = "#0b0b0b"
PASTA_FIGURAS = Path(__file__).resolve().parent / "figuras"


def estilo():
    plt.rcParams.update({
        "figure.facecolor": FUNDO,
        "axes.facecolor": FUNDO,
        "axes.edgecolor": "#b9b8b3",
        "axes.labelcolor": TEXTO,
        "axes.titlesize": 12,
        "axes.titleweight": "bold",
        "axes.labelsize": 10,
        "xtick.color": NEUTRA,
        "ytick.color": NEUTRA,
        "axes.grid": True,
        "grid.color": "#e4e3df",
        "grid.linewidth": 0.6,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "legend.frameon": False,
        "font.size": 10,
    })


def salvar(figura, nome):
    PASTA_FIGURAS.mkdir(exist_ok=True)
    caminho = PASTA_FIGURAS / nome
    figura.savefig(caminho, dpi=150, bbox_inches="tight")
    return caminho
