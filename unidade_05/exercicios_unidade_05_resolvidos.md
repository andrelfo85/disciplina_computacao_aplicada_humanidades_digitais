# U05-A08 — Exercícios de múltipla escolha — Unidade 5

> **Resolução.** A alternativa escolhida está marcada com [x] e justificada abaixo de cada questão. As respostas foram dadas antes da consulta ao gabarito da disciplina e depois conferidas com ele.

Assinale uma alternativa e justifique antes de consultar o gabarito.

## Questão 1

Ao comparar a extensão de documentos com forte assimetria e um valor extremo, qual prática é mais defensável?

- [ ] **A.** Relatar apenas a média
- [x] **B.** Relatar média, mediana, distribuição e casos influentes
- [ ] **C.** Remover o extremo automaticamente
- [ ] **D.** Substituir palavras por proporções

**Justificativa:** Com assimetria e extremo, uma única medida esconde a forma; média, mediana, distribuição e casos influentes devem aparecer juntos.

## Questão 2

Capital tem média 600 e Interior 500 palavras. Qual é Capital menos Interior?

- [x] **A.** 100 palavras e 20% de Interior
- [ ] **B.** 100 palavras e 16,7% de Capital
- [ ] **C.** -100 palavras e 20% de Interior
- [ ] **D.** 1,2 palavra

**Justificativa:** 600 − 500 = 100 palavras; tomando Interior como referência, 100/500 = 0,20, ou 20%.

## Questão 3

O que a variabilidade amostral descreve?

- [ ] **A.** Todo erro nos dados
- [ ] **B.** A mudança histórica real
- [x] **C.** A variação da estatística entre amostras sob um procedimento
- [ ] **D.** A probabilidade de a hipótese ser verdadeira

**Justificativa:** Variabilidade amostral é a variação de uma estatística entre amostras obtidas pelo mesmo procedimento; não é todo erro nem mudança histórica.

## Questão 4

Qual interpretação de um IC de 95% é adequada?

- [ ] **A.** 95% dos dados estão dentro dele
- [ ] **B.** Há 95% de probabilidade frequentista de o parâmetro fixo estar nele
- [x] **C.** Em repetições, cerca de 95% dos intervalos do procedimento cobririam o parâmetro
- [ ] **D.** A hipótese nula tem 5% de chance

**Justificativa:** A confiança se refere ao procedimento: em repetições, cerca de 95% dos intervalos construídos assim cobririam o parâmetro.

## Questão 5

Em um teste de permutação, o que gera a distribuição de referência?

- [ ] **A.** Remover extremos
- [x] **B.** Embaralhar rótulos sob intercambiabilidade nula
- [ ] **C.** Ordenar valores
- [ ] **D.** Aumentar artificialmente a amostra

**Justificativa:** Sob a hipótese nula de rótulos intercambiáveis, embaralhar os rótulos gera a distribuição de referência.

## Questão 6

Um valor de p de 0,03 significa que:

- [ ] **A.** a hipótese nula tem 3% de chance
- [ ] **B.** o efeito é importante
- [x] **C.** sob o modelo nulo, resultados tão extremos ocorreriam com baixa frequência
- [ ] **D.** há 97% de replicação

**Justificativa:** O valor de p indica quão raros seriam resultados tão extremos sob o modelo nulo; não é a probabilidade da hipótese nula (Wasserstein e Lazar, 2016).

## Questão 7

Por que relatar tamanho de efeito e escala original?

- [ ] **A.** Para substituir o desenho
- [x] **B.** Para descrever magnitude, não apenas compatibilidade com o nulo
- [ ] **C.** Para provar causalidade
- [ ] **D.** Para tornar o p menor

**Justificativa:** O tamanho de efeito e a escala original informam a magnitude, que o valor de p não informa.

## Questão 8

Uma diferença estatisticamente detectável é substantivamente relevante quando:

- [ ] **A.** p < 0,05
- [ ] **B.** a amostra é grande
- [x] **C.** a magnitude importa para a pergunta e o contexto
- [ ] **D.** o intervalo é estreito

**Justificativa:** A relevância depende da magnitude em relação à pergunta e ao contexto, não do limiar de 0,05 nem do tamanho da amostra.

## Questão 9

O que uma representação Bag of Words perde diretamente?

- [ ] **A.** Frequências
- [ ] **B.** Identificador
- [x] **C.** Ordem e grande parte da sintaxe
- [ ] **D.** Vocabulário

**Justificativa:** Bag of Words guarda frequências e descarta ordem e grande parte da sintaxe.

## Questão 10

Em uma matriz documento-termo, uma linha representa normalmente:

- [ ] **A.** um termo
- [x] **B.** um documento ou unidade textual declarada
- [ ] **C.** um teste
- [ ] **D.** uma hipótese

**Justificativa:** Na matriz documento-termo, linhas são documentos (ou unidades textuais declaradas) e colunas são termos.

## Questão 11

O que aumenta o IDF na convenção apresentada?

- [ ] **A.** O termo aparecer em muitos documentos
- [x] **B.** O termo ser relativamente raro na coleção
- [ ] **C.** O documento ser longo
- [ ] **D.** A ordem do termo

**Justificativa:** O IDF cresce quando o termo aparece em poucos documentos da coleção.

## Questão 12

Um termo com TF-IDF alto é necessariamente historicamente importante?

- [ ] **A.** Sim
- [ ] **B.** Somente se p < 0,05
- [x] **C.** Não; é frequente localmente e raro na coleção sob uma convenção
- [ ] **D.** Somente em textos longos

**Justificativa:** Um TF-IDF alto indica termo frequente no documento e raro na coleção sob uma convenção; não prova importância histórica.

## Questão 13

Jaccard entre {a,b,c} e {b,c,d} é:

- [ ] **A.** 1/4
- [ ] **B.** 2/3
- [x] **C.** 2/4
- [ ] **D.** 3/4

**Justificativa:** Interseção {b, c} tem 2 elementos; união {a, b, c, d} tem 4; J = 2/4 = 0,5.

## Questão 14

O cosseno compara principalmente:

- [x] **A.** o ângulo entre vetores
- [ ] **B.** a ordem dos caracteres
- [ ] **C.** a significância estatística
- [ ] **D.** a autoria real

**Justificativa:** O cosseno mede o ângulo entre vetores, reduzindo o efeito da magnitude total.

## Questão 15

Por que Jaccard e cosseno podem ordenar textos diferentemente?

- [ ] **A.** Um deles sempre está errado
- [x] **B.** Presença, frequência e ponderação preservam informações diferentes
- [ ] **C.** Cosseno lê contexto
- [ ] **D.** Jaccard testa hipóteses

**Justificativa:** Jaccard usa só presença; o cosseno usa frequências ou pesos; cada um preserva informação diferente.

## Questão 16

A distância de edição mínima conta:

- [ ] **A.** tópicos
- [x] **B.** inserções, exclusões e substituições
- [ ] **C.** termos raros
- [ ] **D.** intervalos

**Justificativa:** A distância de Levenshtein conta o menor número de inserções, exclusões e substituições.

## Questão 17

Qual uso é mais adequado para distância de edição?

- [ ] **A.** Provar autoria
- [x] **B.** Comparar duas versões próximas de uma transcrição
- [ ] **C.** Medir relevância social
- [ ] **D.** Comparar médias

**Justificativa:** É adequada para comparar versões próximas de uma mesma sequência, como duas transcrições.

## Questão 18

Para comparar autores, períodos ou coleções, qual cautela é central?

- [ ] **A.** Unir tudo sem metadados
- [x] **B.** Documentar unidade, composição e possíveis fatores de confusão
- [ ] **C.** Usar apenas o vizinho mais próximo
- [ ] **D.** Ignorar gênero

**Justificativa:** É preciso documentar a unidade, a composição dos grupos e possíveis fatores de confusão (gênero, período, transcrição).

## Questão 19

Ao encontrar o documento mais semelhante, o próximo passo é:

- [ ] **A.** Concluir equivalência semântica
- [x] **B.** Inspecionar textos, metadados e casos divergentes
- [ ] **C.** Remover os demais
- [ ] **D.** Inferir causalidade

**Justificativa:** Uma alta similaridade é ponto de partida para inspecionar textos, metadados e divergências.

## Questão 20

Uma comparação de versões com distância normalizada deve declarar:

- [ ] **A.** apenas o menor número
- [x] **B.** unidade, custos e denominador de normalização
- [ ] **C.** um valor de p
- [ ] **D.** uma causa histórica

**Justificativa:** A distância normalizada só é interpretável com unidade (caractere ou token), custos e denominador declarados.
