
**Introdução**

Explicação da abordagem para resolução do TPC2.

**Informações**
* Nome: Gonçalo Campos Pereira
* Número: pg53834

**Problema**

Estrutar a informação resultante do programa *word_freq* do TPC1 numa tabela de frequências, limpar essa mesma informação (por exemplo, eliminando palavras com números), e comparar rácios de ocorrências de diferentes textos.

**Solução**
* Criação da função *import_db* para carregar o ficheiro da base de dados. Esse ficheiro encontra-se na diretoria *tests* e corresponde à tabela de ocorrências das palavras da língua portuguesa.
* Criação da função *compare* que para cada palavra presente no texto em questão (neste caso, uma vez mais, *Amor de Perdição* de Camilo Castelo Branco) calcula a sua frequência relativa no mesmo, e na base de dados. O valor final apresentado é a divisão destes dois valores. No caso da palavra não se encontra na base de dados, considera-se que tem 1 ocorrência.
* Sendo este uma continuação do código do TPC1, as opções que o programa oferece são as mesmas, tendo sido adicionada apenas a opção -t que mostra o resultado da freqência referida acima, para cada palavra do texto.

O programa executa através da invocação do seguinte comando:
    
    word_freq.py [opção] ficheiro_input
