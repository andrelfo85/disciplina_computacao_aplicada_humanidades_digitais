"""Reconstrução reproduzível da base do projeto Goodreads.

Projeto: desigualdade de gênero no reconhecimento literário em uma rede social
de catalogação e avaliação de livros (Goodreads).

Fluxo: dados/brutos (imutável) -> dados/intermediarios -> dados/derivados.
Nenhuma função altera o arquivo bruto. Cada transformação preserva o valor
original em uma coluna própria e registra a regra aplicada.

Uso:
    python preparar_base.py            # reconstrói tudo e executa os testes
    from preparar_base import construir_base
"""

from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parent
BRUTO = RAIZ / "dados" / "brutos" / "livros_good_reads.csv"
INTERMEDIARIOS = RAIZ / "dados" / "intermediarios"
DERIVADOS = RAIZ / "dados" / "derivados"
SHA256_ESPERADO = "40effdd64def421fbd9b6665542ebfbf058ad3c6c902acfba96227763b9cfe64"

COLUNAS_ESPERADAS = [
    "id_livro", "titulo", "id_autor", "genero_1", "genero_2", "paginas",
    "ano_publicacao", "nota_livro", "n_avaliacoes", "n_resenhas", "autor",
    "genero_autor", "pais_nascimento", "nota_autor", "n_avaliacoes_autor",
]

# ---------------------------------------------------------------------------
# Regras de padronização do local de nascimento.
# O valor original é sempre preservado em `pais_original`.
# ---------------------------------------------------------------------------
LOCAIS_EUA = {
    "AZ", "Alabama", "Alaska", "Baltimore", "Boston", "Brooklyn", "CA", "CT",
    "California", "Chicago", "Cleveland", "Colorado", "D.C.", "DC", "Dallas",
    "Delaware", "Ft. Lauderdale", "Hawaii", "IL", "Illinois", "Indiana",
    "Indianapolis", "KS", "KY", "Kentucky", "Los Angeles", "MA", "MN",
    "Manhattan", "Maryland", "Massachusetts", "Michigan", "Minneapolis",
    "Minnesota", "Minot", "Missouri", "NH", "NY", "New Jersey", "New Orleans",
    "New York", "New York City", "OH", "Ohio", "PA", "Philadelphia",
    "Rhode Island", "Rocky Mount", "Salt Lake City", "San Francisco", "Seattle",
    "Somewhere snowy MN", "South Dakota", "Southern California", "TX", "VA",
    "Virginia", "Westminister CA", "Wichita Falls",
}
LOCAIS_REINO_UNIDO = {
    "England", "Scotland", "Wales", "Northern Ireland", "London",
    "Buckinghamshire",
}
EQUIVALENCIAS_DIRETAS = {
    "French Republic": "France",
    "now Pakistan": "Pakistan",
    "Winnipeg": "Canada",
    "Seoul": "South Korea",
}
LOCAIS_AMBIGUOS = {"Georgia", "Birmingham", "Melbourne", "Springfield", "Jerusalem"}
ENTIDADES_HISTORICAS_OU_INCOMPLETAS = {
    "USSR", "Russian Empire", "Austria-Hungary", "Kingdom of France",
    "British India", "Czechoslovakia", "the Former Yugoslav Republic of",
    "Occupied", "Republic of",
}
VALORES_INVALIDOS = {
    "http://nikkiloftin.com/": "URL no lugar do local",
    "a phoenix egg": "valor ficcional ou humorístico",
    "Identity of author to remamystery for now": "identidade da autoria declarada como oculta",
    "Antarctica": "local implausível para nascimento, sem confirmação",
    "currently living Canada": "informa residência, não nascimento",
}


def sha256_arquivo(caminho: Path) -> str:
    h = hashlib.sha256()
    with open(caminho, "rb") as arquivo:
        for bloco in iter(lambda: arquivo.read(65536), b""):
            h.update(bloco)
    return h.hexdigest()


def ler_bruto(caminho: Path = BRUTO) -> pd.DataFrame:
    """Lê o CSV bruto com parâmetros explícitos (UTF-8 com BOM, vírgula)."""
    return pd.read_csv(caminho, sep=",", encoding="utf-8-sig")


def chave_textual(valor: str) -> str:
    """Chave de comparação que preserva letras de qualquer alfabeto.

    Remove o marcador de série entre parênteses, acentos e pontuação. A versão
    inicial desta regra usava apenas [a-z0-9] e apagava títulos em árabe e
    persa, criando falsas duplicatas; por isso a classe \\w (Unicode) é usada.
    """
    texto = re.sub(r"\s*\(.*?\)\s*", " ", str(valor))
    texto = unicodedata.normalize("NFKD", texto.casefold())
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    return " ".join(re.findall(r"\w+", texto))


def padronizar_local(valor: str) -> tuple:
    """Retorna (pais_padronizado, regra_aplicada)."""
    if pd.isna(valor):
        return (pd.NA, "ausente no bruto")
    if valor in VALORES_INVALIDOS:
        return (pd.NA, "inválido: " + VALORES_INVALIDOS[valor])
    if valor in LOCAIS_EUA:
        return ("United States", "cidade ou estado dos EUA agregado ao país")
    if valor in LOCAIS_REINO_UNIDO:
        return ("United Kingdom", "nação constituinte ou cidade agregada ao Reino Unido")
    if valor in EQUIVALENCIAS_DIRETAS:
        return (EQUIVALENCIAS_DIRETAS[valor], "equivalência direta documentada")
    if valor in LOCAIS_AMBIGUOS:
        return (pd.NA, "ambíguo: pode corresponder a mais de um país")
    if valor in ENTIDADES_HISTORICAS_OU_INCOMPLETAS:
        return (valor, "entidade histórica ou nome incompleto mantido sem correspondência atual")
    return (valor, "mantido")


PADRAO_INICIAIS = re.compile(r"([A-Za-z]\.)+[A-Za-z]?")


def primeiro_prenome(nome: str):
    """Primeiro elemento do nome que não seja inicial.

    'Mary Ann Evans' -> 'Mary'; 'W. Bruce Cameron' -> 'Bruce'.
    Se, depois de retirar as iniciais, sobrar apenas o sobrenome
    ('J.R. Ward', 'C.S. Lewis'), não há prenome classificável: retorna None.
    Nomes de uma só palavra ('Homer') são mantidos.
    """
    partes = [p.strip(".,") for p in str(nome).split() if p.strip(".,")]
    sem_iniciais = [
        p for p in partes
        if not (len(p.replace(".", "")) <= 1 or PADRAO_INICIAIS.fullmatch(p))
    ]
    if not sem_iniciais:
        return None
    if len(sem_iniciais) == 1 and len(partes) > 1:
        return None
    return sem_iniciais[0]


def inferir_genero_por_nome(autores: pd.DataFrame) -> pd.DataFrame:
    """Infere o gênero associado ao prenome com o pacote gender-guesser.

    A inferência NÃO identifica o gênero de uma pessoa. Ela estima como um
    prenome costuma ser classificado em um dicionário de nomes (Jörg Michael,
    2007-2008, distribuído no pacote gender-guesser). Serve apenas para auditar
    o campo `genero_autor`. Se o pacote não estiver instalado, usa a auditoria
    previamente gravada em dados/derivados/auditoria_genero_nome.csv.
    """
    try:
        import gender_guesser.detector as detector_genero
        detector = detector_genero.Detector(case_sensitive=False)
        prenomes = autores["autor"].map(primeiro_prenome)
        resultado = prenomes.map(lambda p: detector.get_gender(p) if p else "sem_prenome")
        return pd.DataFrame({
            "id_autor": autores["id_autor"].to_numpy(),
            "prenome_usado": prenomes.to_numpy(),
            "genero_por_nome": resultado.to_numpy(),
            "ferramenta": "gender-guesser 0.4.0 (dicionário de nomes de Jörg Michael, versão 2007-2008)",
        })
    except ImportError:
        cache = DERIVADOS / "auditoria_genero_nome.csv"
        if not cache.exists():
            raise ImportError(
                "Instale gender-guesser (pip install gender-guesser) ou forneça "
                "dados/derivados/auditoria_genero_nome.csv"
            )
        gravado = pd.read_csv(cache)
        return gravado[["id_autor", "prenome_usado", "genero_por_nome", "ferramenta"]]


def normalizar(bruto: pd.DataFrame) -> pd.DataFrame:
    """Cria a camada intermediária: originais preservados, regras explícitas."""
    t = bruto.copy()
    # Texto
    t["titulo_chave"] = t["titulo"].map(chave_textual)
    t["titulo_tem_marcador_serie"] = t["titulo"].str.contains(r"#\s?\d", regex=True)
    t["titulo_sem_letra_latina"] = ~t["titulo"].str.contains(r"[A-Za-z]", regex=True)
    # Local de nascimento
    t["pais_original"] = t["pais_nascimento"]
    locais = t["pais_original"].map(padronizar_local)
    t["pais_padronizado"] = locais.map(lambda x: x[0])
    t["regra_pais"] = locais.map(lambda x: x[1])
    t["nascido_eua"] = t["pais_padronizado"].eq("United States").astype("boolean")
    t.loc[t["pais_padronizado"].isna(), "nascido_eua"] = pd.NA
    # Datas: ano negativo indica a.C.; nada é inventado
    t["ano_original"] = t["ano_publicacao"]
    t["ano_antes_de_1900"] = t["ano_publicacao"] < 1900
    t["periodo_publicacao"] = pd.cut(
        t["ano_publicacao"],
        bins=[-10_000, 1899, 1989, 2009, 2019],
        labels=["antes de 1900", "1900-1989", "1990-2009", "2010-2019"],
    )
    # Páginas: sinalizar, não corrigir
    t["paginas_suspeitas"] = (t["paginas"] <= 10) | (t["paginas"] > 2000)
    # Coerência entre contagens do livro e do autor
    t["contagem_livro_maior_que_autor"] = t["n_avaliacoes"] > t["n_avaliacoes_autor"]
    # Medidas derivadas de reconhecimento
    t["taxa_resenhas"] = t["n_resenhas"] / t["n_avaliacoes"]
    t["log10_avaliacoes"] = np.log10(t["n_avaliacoes"])
    t["log10_resenhas_mais_1"] = np.log10(t["n_resenhas"] + 1)
    # Possíveis duplicatas: mesma chave de título E mesmo autor
    t["possivel_duplicata"] = t.duplicated(["titulo_chave", "id_autor"], keep=False)
    t["titulo_repetido_outro_autor"] = (
        t.duplicated("titulo_chave", keep=False) & ~t["possivel_duplicata"]
    )
    return t


def construir_tabelas(intermediario: pd.DataFrame, auditoria_nome: pd.DataFrame) -> dict:
    """Separa entidades e relações e cria as especificações de gênero."""
    colunas_livro = [
        "id_livro", "titulo", "titulo_chave", "id_autor", "paginas",
        "ano_publicacao", "periodo_publicacao", "nota_livro", "n_avaliacoes",
        "n_resenhas", "taxa_resenhas", "log10_avaliacoes",
        "log10_resenhas_mais_1", "titulo_tem_marcador_serie",
        "titulo_sem_letra_latina", "ano_antes_de_1900", "paginas_suspeitas",
        "contagem_livro_maior_que_autor", "possivel_duplicata",
        "titulo_repetido_outro_autor",
    ]
    livros = intermediario[colunas_livro].copy()

    autores = (
        intermediario[[
            "id_autor", "autor", "genero_autor", "pais_original",
            "pais_padronizado", "regra_pais", "nascido_eua", "nota_autor",
            "n_avaliacoes_autor",
        ]]
        .drop_duplicates("id_autor")
        .rename(columns={"genero_autor": "genero_autor_original"})
        .reset_index(drop=True)
    )
    autores = autores.merge(auditoria_nome, on="id_autor", how="left", validate="one_to_one")
    # Auditoria: rótulo 'masculino' com prenome classificado como feminino
    autores["rotulo_duvidoso"] = (
        autores["genero_autor_original"].eq("masculino")
        & autores["genero_por_nome"].isin(["female", "mostly_female"])
    )
    autores["conflito_inverso"] = (
        autores["genero_autor_original"].eq("feminino")
        & autores["genero_por_nome"].isin(["male", "mostly_male"])
    )
    # E1: rótulo original
    autores["genero_E1_original"] = autores["genero_autor_original"]
    # E2 (principal): exclui rótulos duvidosos (NA)
    autores["genero_E2_sem_duvidosos"] = autores["genero_autor_original"].where(
        ~autores["rotulo_duvidoso"], pd.NA
    )
    # E3: reclassifica rótulos duvidosos como feminino (pressuposto forte)
    autores["genero_E3_reclassificado"] = autores["genero_autor_original"].where(
        ~autores["rotulo_duvidoso"], "feminino"
    )

    livro_generos = intermediario.melt(
        id_vars="id_livro", value_vars=["genero_1", "genero_2"],
        var_name="posicao", value_name="genero_literario",
    )
    livro_generos["posicao"] = livro_generos["posicao"].map({"genero_1": 1, "genero_2": 2})
    livro_generos = livro_generos.sort_values(["id_livro", "posicao"]).reset_index(drop=True)

    # Base analítica: um livro por linha, com atributos do autor (N:1)
    base = livros.merge(
        intermediario[["id_livro", "genero_1", "genero_2"]],
        on="id_livro", how="left", validate="one_to_one",
    ).merge(autores, on="id_autor", how="left", validate="many_to_one", indicator=True)

    return {"livros": livros, "autores": autores, "livro_generos": livro_generos, "base_analitica": base}


def testar(bruto: pd.DataFrame, tabelas: dict) -> pd.Series:
    """Testes de esquema, domínio, chaves e cardinalidade."""
    base = tabelas["base_analitica"]
    autores = tabelas["autores"]
    testes = {
        "hash_bruto_confere": sha256_arquivo(BRUTO) == SHA256_ESPERADO,
        "colunas_esperadas": list(bruto.columns) == COLUNAS_ESPERADAS,
        "id_livro_unico": bruto["id_livro"].is_unique,
        "sem_valores_ausentes_no_bruto": int(bruto.isna().sum().sum()) == 0,
        "genero_autor_binario": set(bruto["genero_autor"]) == {"feminino", "masculino"},
        "notas_entre_1_e_5": bool(bruto["nota_livro"].between(1, 5).all()),
        "resenhas_nao_excedem_avaliacoes": bool((bruto["n_resenhas"] <= bruto["n_avaliacoes"]).all()),
        "atributos_do_autor_constantes": bool(
            (bruto.groupby("id_autor")[["autor", "genero_autor", "pais_nascimento", "nota_autor", "n_avaliacoes_autor"]].nunique() == 1).all().all()
        ),
        "juncao_preservou_livros": len(base) == len(bruto),
        "todos_os_livros_tem_autor": bool(base["_merge"].eq("both").all()),
        "id_autor_unico_na_tabela_autores": autores["id_autor"].is_unique,
        "relacoes_livro_genero_2_por_livro": len(tabelas["livro_generos"]) == 2 * len(bruto),
    }
    return pd.Series(testes, name="resultado")


def construir_base(gravar: bool = True) -> dict:
    bruto = ler_bruto()
    intermediario = normalizar(bruto)
    autores_unicos = bruto.drop_duplicates("id_autor")[["id_autor", "autor"]]
    auditoria_nome = inferir_genero_por_nome(autores_unicos)
    tabelas = construir_tabelas(intermediario, auditoria_nome)
    tabelas["testes"] = testar(bruto, tabelas)
    if gravar:
        INTERMEDIARIOS.mkdir(parents=True, exist_ok=True)
        DERIVADOS.mkdir(parents=True, exist_ok=True)
        intermediario.to_csv(INTERMEDIARIOS / "livros_normalizado.csv", index=False)
        auditoria_nome.to_csv(DERIVADOS / "auditoria_genero_nome.csv", index=False)
        tabelas["livros"].to_csv(DERIVADOS / "livros.csv", index=False)
        tabelas["autores"].to_csv(DERIVADOS / "autores.csv", index=False)
        tabelas["livro_generos"].to_csv(DERIVADOS / "livro_generos.csv", index=False)
        tabelas["base_analitica"].drop(columns="_merge").to_csv(
            DERIVADOS / "base_analitica.csv", index=False
        )
        log = {
            "entrada": str(BRUTO.relative_to(RAIZ)),
            "sha256_entrada": SHA256_ESPERADO,
            "pandas": pd.__version__,
            "numpy": np.__version__,
            "auditoria_genero_por_nome": "gender-guesser 0.4.0, dicionário de nomes de Jörg Michael (2007-2008); uso restrito à auditoria do rótulo",
            "saidas": sorted(p.name for p in DERIVADOS.glob("*.csv")),
            "testes": {k: bool(v) for k, v in tabelas["testes"].items()},
        }
        (DERIVADOS / "log_execucao.json").write_text(
            json.dumps(log, ensure_ascii=False, indent=2), encoding="utf-8"
        )
    return tabelas


def carregar_base_analitica() -> pd.DataFrame:
    """Lê a base analítica derivada; reconstrói se ela não existir."""
    caminho = DERIVADOS / "base_analitica.csv"
    if not caminho.exists():
        construir_base(gravar=True)
    base = pd.read_csv(caminho)
    ordem = ["antes de 1900", "1900-1989", "1990-2009", "2010-2019"]
    base["periodo_publicacao"] = pd.Categorical(base["periodo_publicacao"], categories=ordem, ordered=True)
    return base


if __name__ == "__main__":
    resultado = construir_base(gravar=True)
    print(resultado["testes"])
    print("Todos os testes passaram:", bool(resultado["testes"].all()))
