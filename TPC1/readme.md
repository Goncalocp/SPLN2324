
**Introdução**

Explicação da abordagem para resolução do TPC1.

**Informações**
* Nome: Gonçalo Campos Pereira
* Número: pg53834

**Problema**

Com o auxílio das bibliotecas de Python *jjcli* e *colections*, elaborar um programa que apresenta o número de ocurrências de cada palavra num texto.

**Solução**
* Criação da função *tokenizer* utiliza uma expressão regular para captar as diferentes palavras.
* Criação da função *my_print* que imprime o as palavras e o respetivo número de ocorrências, uma por linha. A função usa também duas variáveis, uma para o comprimento da maior palavra no texto e outra para o comprimento do número de ocorrências mais alto, de forma a ajustar a largura das colunas impressas, resultando numa melhor legibilidade. 
* O tipo de informação impressa varia consoante as opções selecionadas no input, sendo estas as seguintes:
    * -m x : Mostra as x palavras mais comuns
    * -n : Ordenado alfabeticamente (letra maiúscula primeiro)
    * -o : Ordenado pelo número de ocorrências (ascendente)
    * -p : Ordenado pelo número de ocorrências (descendente)
    * -q : Palavra primeiro e só depois o seu número de ocorrências

O programa executa através da invocação do seguinte comando:
    
    pyton3 word_freq.py [opção] ficheiro_input


Nota: Neste caso, o texto escolhido e fornecido pela equipa docente foi *Amor de Perdição* de Camilo Castelo Branco, porém, o programa funciona para qualquer texto.
