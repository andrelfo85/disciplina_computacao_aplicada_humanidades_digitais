# Resolução das atividades: Unidades 1 a 5

**Disciplina:** Computação Aplicada a Problemas em Humanidades Digitais
(repositório `lalvim/disciplina_computacao_aplicada_humanidades_digitais`).

**Tema do projeto:** desigualdade de gênero no reconhecimento literário em
redes sociais de catalogação e avaliação de livros. Pergunta: no Goodreads,
livros escritos por mulheres recebem o mesmo reconhecimento que livros escritos
por homens? O projeto não julga a qualidade da escrita; examina a distribuição
do reconhecimento (avaliações, resenhas) e sua variação por gênero literário.

**Base:** `projeto_goodreads/dados/brutos/livros_good_reads.csv` (10.454 livros,
15 colunas, SHA-256 `40effdd64def421fbd9b6665542ebfbf058ad3c6c902acfba96227763b9cfe64`).

## Onde estão as respostas

Todas as atividades foram resolvidas **dentro dos próprios notebooks**, no lugar
dos campos “Escreva aqui”. Quando a atividade exigia cálculo com os dados do
projeto, foram acrescentadas seções **“Aplicação ao projeto Goodreads”** com
código executado. Os exercícios de múltipla escolha estão em arquivos
`exercicios_unidade_0X_resolvidos.md`, com a alternativa marcada e
justificada.

| Unidade | Atividades | Arquivos |
|---|---|---|
| 1 | U01-A01 a U01-A13 (notebooks) e U01-A14 (múltipla escolha) | `unidade_01/0*.ipynb`, `unidade_01/exercicios_unidade_01_resolvidos.md` |
| 2 | U02-A01 a U02-A11 e U02-A12 | `unidade_02/0*.ipynb`, `unidade_02/exercicios_unidade_02_resolvidos.md` |
| 3 | U03-A01 a U03-A06 e U03-A07 | `unidade_03/0*.ipynb`, `unidade_03/exercicios_unidade_03_resolvidos.md` |
| 4 | U04-A01 a U04-A06 e U04-A07 | `unidade_04/0*.ipynb`, `unidade_04/exercicios_unidade_04_resolvidos.md` |
| 5 | U05-A01 a U05-A07 e U05-A08 | `unidade_05/0*.ipynb`, `unidade_05/exercicios_unidade_05_resolvidos.md` |

As atividades guiadas que usam os dados fictícios da disciplina (por exemplo,
U01-A03, U01-A07, U02-A02, U02-A04, U02-A07) foram respondidas sobre esses
dados, como pede o enunciado, e, quando cabível, repetidas com os dados do
Goodreads.

## Como reproduzir

1. Instale as dependências: `pip install -r requirements.txt gender-guesser`
   (a análise foi executada com pandas 2.3.3, numpy 2.5.3, matplotlib 3.11 e
   gender-guesser 0.4.0).
2. Reconstrua a base: dentro de `projeto_goodreads/`, rode
   `python preparar_base.py` (12 testes automáticos; todos passam).
3. Execute os notebooks em ordem, da Unidade 1 à 5, cada um do início ao fim.
   A pasta `projeto_goodreads/` precisa ficar ao lado das pastas `unidade_0X`.
   No Google Colab, envie a pasta `projeto_goodreads` para `/content`.

Todos os 27 notebooks foram executados do início ao fim sem erros, e as saídas
estão gravadas nos arquivos.

## Principais resultados

1. **Auditoria do rótulo de gênero (Unidade 3).** O campo `genero_autor` tem
   erro sistemático: 886 dos 3.230 autores cujo prenome é classificado como
   feminino por um dicionário de nomes (27,4%) estão rotulados como
   “masculino” (por exemplo, Janet Evanovich, Diana Gabaldon, Alice Sebold,
   Paula Hawkins). A análise usa três especificações: E1 (rótulo original), E2
   (principal, sem os 1.274 livros com rótulo duvidoso) e E3 (duvidosos
   reclassificados como feminino).
2. **Diferença agregada (Unidades 4 e 5).** Em E2, a mediana de avaliações é
   3.129 para livros de autoras e 5.218 para livros de autores (razão de 0,60).
   Em log10, a diferença é −0,176, com intervalo bootstrap por autor de
   [−0,225; −0,124].
3. **Composição temporal.** Entre livros publicados de 2010 a 2019, a relação
   se inverte: a mediana dos livros de autoras é 1,46 vez a dos livros de
   autores. Comparando livros do mesmo ano (1990–2018), os de autoras recebem
   mais avaliações (+0,131 em log10). A diferença agregada reflete sobretudo um
   cânone antigo, muito avaliado e majoritariamente masculino (80% dos
   clássicos do recorte).
4. **Gênero literário.** A participação de autoras varia de 11% (History) a 91%
   (New Adult). Entre livros de 2010 a 2019, só não ficção e ficção científica
   continuam com mediana maior para livros de autores.
5. **Resenhas.** A taxa de resenhas por avaliação é maior entre livros de
   autoras no agregado (0,114 contra 0,076), mas a diferença desaparece quando
   se compara dentro de cada ano.
6. **Títulos.** Títulos de autoras usam mais *love*, *girl* e *woman*; títulos
   de autores, mais *war*, *man* e *world*, o que acompanha convenções de
   gênero literário.

Todos esses resultados valem apenas para o recorte, cujo critério de seleção e
data de coleta são desconhecidos.

## Avisos de honestidade e pontos a verificar

- **Atividades em dupla, trio ou revisão por pares** (U01-A04, A05, A13;
  U02-A08, A09 parte D, A11; U03-A06; U04-A06; U05-A02 a A07) foram resolvidas
  com uma **revisão crítica simulada**, identificada como tal em cada
  notebook. Ela não substitui o parecer de colegas reais.
- **Campos pessoais** (nome do estudante, experiência com Python) foram
  deixados para preenchimento, porque essas informações não foram fornecidas.
- **Proveniência do CSV:** não foi possível identificar a fonte original do
  arquivo; isso está registrado em `projeto_goodreads/dados/brutos/proveniencia_goodreads.json`.
- **Referências a conferir:** os fatos sobre a aquisição do Goodreads pela
  Amazon (2013) e o fim das novas chaves de API (dezembro de 2020) vêm de uma
  reportagem do Slashdot (2020); convém confirmar em fonte institucional. O
  volume e o número do artigo de Underwood, Bamman e Lee (2018) não foram
  conferidos. O dado de Dalcastagnè (72,7% de autores homens em 258 romances)
  foi conferido em artigo posterior da autora (2008), que o retoma.
- **Casos de autores famosos** usados para ilustrar o erro do rótulo de gênero
  se baseiam em conhecimento público e devem ser conferidos em biografias.
- **Travessões longos:** os textos desta resolução não usam travessão longo. Os
  que aparecem em títulos e enunciados das atividades pertencem ao material
  original da disciplina e foram mantidos sem alteração.

## Referências mobilizadas na resolução

Além das referências da própria disciplina (listadas nos arquivos
`referencias.md` de cada unidade), foram verificadas e usadas:

- DALCASTAGNÈ, Regina (2005). A personagem do romance brasileiro
  contemporâneo: 1990-2004. *Estudos de Literatura Brasileira
  Contemporânea*, n. 26, p. 13–71.
- MERTON, Robert K. (1968). The Matthew Effect in Science. *Science*, v. 159,
  n. 3810, p. 56–63. DOI: 10.1126/science.159.3810.56.
- ROSSITER, Margaret W. (1993). The Matthew Matilda Effect in Science.
  *Social Studies of Science*, v. 23, n. 2, p. 325–341. DOI:
  10.1177/030631293023002004.
- SABRI, Nazanin; WEBER, Ingmar (2021). A Global Book Reading Dataset.
  *Data*, v. 6, n. 8, art. 83. DOI: 10.3390/data6080083.
- SANTAMARÍA, Lucía; MIHALJEVIĆ, Helena (2018). Comparison and benchmark of
  name-to-gender inference services. *PeerJ Computer Science*, v. 4, e156.
  DOI: 10.7717/peerj-cs.156.
- THELWALL, Mike (2017). Book genre and author gender:
  Romance>Paranormal-Romance to Autobiography>Memoir. *Journal of the
  Association for Information Science and Technology*, v. 68, n. 5,
  p. 1212–1223. DOI: 10.1002/asi.23768.
- THELWALL, Mike (2019). Reader and author gender and genre in Goodreads.
  *Journal of Librarianship and Information Science*, v. 51, n. 2,
  p. 403–430. DOI: 10.1177/0961000617709061.
- UNDERWOOD, Ted; BAMMAN, David; LEE, Sabrina (2018). The Transformation of
  Gender in English-Language Fiction. *Journal of Cultural Analytics*.
- VERBOORD, Marc (2012). Female bestsellers: a cross-national study of gender
  inequality and the popular–highbrow culture divide in fiction book
  production, 1960–2009. *European Journal of Communication*, v. 27, n. 4,
  p. 395–409. DOI: 10.1177/0267323112459433.
- BRASIL (2018). Lei nº 13.709 (LGPD), art. 5º, I e II.
- SLASHDOT (2020). Goodreads Is Retiring Its Current API, and Book-Loving
  Developers Aren't Happy. Reportagem de 17 dez. 2020.
