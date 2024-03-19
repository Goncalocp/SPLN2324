**Introdução**

Explicação da abordagem para resolução do TPC5.

**Informações**
* Nome: Gonçalo Campos Pereira
* Número: pg53834

**Problema**

O objetivo do trabalho proposto é utilizar o módulo *SpaCy*, do Python, de forma a apresentar as informações de cada token de uma frase/texto.

**Solução**
Para resolução do problema, foram realizadas as seguintes etapas:

    * Carregar o modelo do SpaCy para a lingua portuguesa
    * Criar objeto (*doc*) que contém a frase/texto processada com o *nlp* do SpaCy
    * Utilizar *retokenizer* (ferramenta do spaCy) que permite modificar os tokens processados inicialmente. Este é bastante útil quando desejamos fazer alterações nos
tokens, como por exemplo, no caso da frase em questão, interpretar "Ponte de Lima" como sendo uma entidade só, e não um conjunto de tokens independentes
    * Percorrer os tokens da variável *doc* para imprimir as suas informações 