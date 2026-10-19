# U03-A07 — Exercícios de múltipla escolha da Unidade 3

> **Resolução.** A alternativa escolhida está marcada com [x] e justificada abaixo de cada questão. As respostas foram dadas antes da consulta ao gabarito da disciplina e depois conferidas com ele.

Marque uma alternativa e consulte o gabarito após concluir.

## Questão 1 — Camadas de dados

Qual prática preserva melhor a auditabilidade?

- [ ] **A.** Editar o CSV recebido
- [x] **B.** Manter brutos imutáveis e gerar derivados
- [ ] **C.** Copiar valores manualmente
- [ ] **D.** Excluir o original após limpar


**Resposta: B.** Brutos imutáveis e derivados reconstruíveis mantêm o caminho de volta à entrada.

## Questão 2 — Estrutura tabular

Em uma tabela de documentos, cada linha deve representar:

- [x] **A.** uma unidade de análise declarada
- [ ] **B.** qualquer quantidade de objetos
- [ ] **C.** uma coluna
- [ ] **D.** um arquivo obrigatoriamente


**Resposta: A.** A estrutura tabular depende de uma unidade de análise declarada para cada linha.

## Questão 3 — Formatos

Qual afirmação sobre PDF é correta?

- [ ] **A.** Sempre contém texto extraível
- [ ] **B.** É equivalente a TXT
- [x] **C.** Pode conter texto, imagem ou ambos
- [ ] **D.** É sempre tabular


**Resposta: C.** Um PDF pode ter camada textual, apenas imagem ou ambos; por isso se diagnostica antes de escolher extração ou OCR.

## Questão 4 — Formatos

Ao importar XLSX, é importante registrar:

- [ ] **A.** somente o tamanho
- [x] **B.** planilha e parâmetros usados
- [ ] **C.** apenas a cor das células
- [ ] **D.** nenhuma decisão


**Resposta: B.** Uma pasta XLSX pode ter várias planilhas; a planilha e os parâmetros lidos precisam ser registrados.

## Questão 5 — Base pública

Por que manter cópia local com data e proveniência?

- [ ] **A.** Porque bases públicas nunca mudam
- [ ] **B.** Para eliminar a fonte
- [x] **C.** Para identificar a versão efetivamente processada
- [ ] **D.** Para evitar citar o produtor


**Resposta: C.** Bases públicas mudam; a cópia local com data e proveniência identifica a versão processada.

## Questão 6 — Extração e OCR

Extração de texto e OCR diferem porque:

- [x] **A.** OCR reconhece caracteres em imagem
- [ ] **B.** extração sempre corrige erros
- [ ] **C.** OCR lê apenas CSV
- [ ] **D.** são operações idênticas


**Resposta: A.** OCR reconhece caracteres a partir de pixels; a extração lê uma camada textual já existente.

## Questão 7 — OCR

Qual procedimento é metodologicamente adequado?

- [ ] **A.** Aceitar toda saída
- [x] **B.** Avaliar uma amostra contra referência
- [ ] **C.** Apagar imagens
- [ ] **D.** Omitir ferramenta e parâmetros


**Resposta: B.** A saída de OCR é hipótese de transcrição e deve ser avaliada contra uma referência (CER e WER).

## Questão 8 — Largo e longo

Ao transformar indicadores largos em longos, muda:

- [ ] **A.** a fonte original
- [x] **B.** a unidade representada por cada linha
- [ ] **C.** a licença
- [ ] **D.** o idioma do texto


**Resposta: B.** No formato longo, cada linha passa a representar uma combinação (por exemplo, documento–tema–período).

## Questão 9 — Normalização

Por que preservar o valor original?

- [ ] **A.** Para impedir qualquer correção
- [x] **B.** Para auditar e eventualmente rever a regra
- [ ] **C.** Para duplicar sem propósito
- [ ] **D.** Para dispensar documentação


**Resposta: B.** Preservar o original permite auditar a regra e revê-la se ela apagar distinções.

## Questão 10 — Códigos

Um código de município deve ser lido preferencialmente como:

- [ ] **A.** medida contínua
- [x] **B.** identificador textual
- [ ] **C.** data
- [ ] **D.** valor monetário


**Resposta: B.** O código municipal identifica uma entidade; não é quantidade sobre a qual se façam contas.

## Questão 11 — Datas e ausências

Converter falhas de data para ausente exige:

- [ ] **A.** apagar o original
- [x] **B.** guardar original e razão da ausência
- [ ] **C.** inventar primeiro dia
- [ ] **D.** excluir a linha


**Resposta: B.** O valor original e a razão da ausência evitam transformar incerteza em falsa exatidão.

## Questão 12 — Duplicatas

Uma possível duplicata deve:

- [ ] **A.** ser apagada automaticamente
- [x] **B.** ser tratada como hipótese para revisão
- [ ] **C.** ser identificada só pelo título
- [ ] **D.** ser ignorada


**Resposta: B.** Semelhança não prova identidade; possíveis duplicatas exigem revisão documental.

## Questão 13 — Junções

O argumento validate='many_to_one' testa:

- [ ] **A.** a cor da tabela
- [x] **B.** a cardinalidade esperada
- [ ] **C.** a qualidade do OCR
- [ ] **D.** o encoding


**Resposta: B.** `validate` testa a cardinalidade declarada e interrompe a junção se ela não se confirmar.

## Questão 14 — Junções

O indicador left_only após uma junção significa:

- [x] **A.** registro da esquerda sem correspondência
- [ ] **B.** duplicata confirmada
- [ ] **C.** linha vazia
- [ ] **D.** erro de sintaxe


**Resposta: A.** `left_only` indica linha da tabela da esquerda sem correspondência na da direita.

## Questão 15 — Integração

Como representar vários temas por documento?

- [ ] **A.** Sobrescrever o tema
- [x] **B.** Tabela relacional documento–tema
- [ ] **C.** Concatenar sem regra
- [ ] **D.** Duplicar todos os metadados manualmente


**Resposta: B.** Uma tabela de relações documento–tema representa a relação 1:N sem repetir o documento.

## Questão 16 — Reprodutibilidade

Um notebook numerado, sozinho:

- [ ] **A.** garante reprodutibilidade total
- [x] **B.** não basta sem ambiente, entradas e testes
- [ ] **C.** elimina proveniência
- [ ] **D.** substitui dados brutos


**Resposta: B.** Reprodutibilidade exige também ambiente, versões, entradas, parâmetros e testes.

## Questão 17 — Limpeza crítica

A expressão 'dados limpos' pode ser problemática porque:

- [ ] **A.** toda transformação é proibida
- [x] **B.** pode ocultar escolhas interpretativas e perdas
- [ ] **C.** CSV não aceita limpeza
- [ ] **D.** dados não têm erros


**Resposta: B.** “Limpar” pode esconder decisões interpretativas e perdas (Rawson e Muñoz, 2019).

## Questão 18 — Integração

Qual produto está pronto para a Unidade 4?

- [ ] **A.** Arquivos sobrescritos sem log
- [x] **B.** Base processável com chaves, testes, log e limites
- [ ] **C.** PDFs sem inventário
- [ ] **D.** Tabela sem unidade declarada

**Resposta: B.** A Unidade 4 precisa de uma base processável com chaves, testes, log e limites documentados.
