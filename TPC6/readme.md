**Introdução**

Explicação da abordagem para resolução do TPC6.

**Informações**
* Nome: Gonçalo Campos Pereira
* Número: pg53834

**Problema**

O objetivo do trabalho proposto é utilizar o módulo *SpaCy*, do Python, de forma a criar uma estrutura que guarde as relações entre as diferentes pessoas/personagens.

**Solução**

Para resolução do problema, foram realizadas as seguintes etapas:

* Carregar o modelo do SpaCy para a lingua portuguesa.
* Carregar o ficheiro que contém o texto a ser analisado (é passado pelo terminal como um argumento do programa).
* Criar objeto (*doc*) que contém a frase/texto processada com o *nlp* do SpaCy.
* Utilizar *retokenizer* (ferramenta do spaCy) que permite modificar os tokens processados inicialmente.
* Percorrer, num ciclo, cada frase do texto e guardar os que são nomes próprios, ou seja, cujo *pos_* seja *PROPN* numa lista. Para cada nome numa frase, é percorrida a lista dos nomes e adicionada a sua relação com os mesmos ao dicionário *friends* ou, caso exista, o valor da relação é incrementado.