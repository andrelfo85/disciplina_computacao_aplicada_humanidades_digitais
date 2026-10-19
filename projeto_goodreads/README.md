# Projeto Goodreads: base do trabalho da disciplina

Pasta com os dados, o código de preparação e as figuras do projeto sobre
desigualdade de gênero no reconhecimento literário no Goodreads, uma rede
social de catalogação e avaliação de livros.

## Estrutura

| Caminho | Conteúdo |
|---|---|
| `dados/brutos/livros_good_reads.csv` | arquivo recebido, somente leitura (não editar) |
| `dados/brutos/proveniencia_goodreads.json` | origem declarada, hash, lacunas de proveniência e restrições |
| `dados/dicionario_dados.csv` | papel, definição, tipo, domínio, origem e limitação dos 15 campos |
| `dados/intermediarios/livros_normalizado.csv` | originais e colunas normalizadas lado a lado |
| `dados/derivados/` | `livros`, `autores`, `livro_generos`, `auditoria_genero_nome`, `base_analitica` e `log_execucao.json` |
| `preparar_base.py` | reconstrói intermediários e derivados a partir do bruto e roda 12 testes |
| `graficos_projeto.py` | estilo e cores dos gráficos |
| `figuras/` | figuras usadas nas Unidades 4 e 5 |

## Reconstrução

```bash
cd projeto_goodreads
python preparar_base.py
```

Requer pandas 2.x, numpy e `gender-guesser` (para a auditoria do rótulo de
gênero por nome). Sem `gender-guesser`, o código usa a auditoria já gravada em
`dados/derivados/auditoria_genero_nome.csv`.

## Especificações de gênero da autoria

| Coluna | Regra |
|---|---|
| `genero_E1_original` | rótulo do arquivo, sem alteração |
| `genero_E2_sem_duvidosos` | rótulo do arquivo; ausente quando o rótulo é “masculino” e o prenome é classificado como feminino (1.274 livros) |
| `genero_E3_reclassificado` | igual a E2, mas os casos duvidosos passam a “feminino” |

A classificação por nome não identifica o gênero de nenhuma pessoa. Ela serve
apenas para auditar o rótulo recebido e não deve ser reutilizada para rotular
autores.
