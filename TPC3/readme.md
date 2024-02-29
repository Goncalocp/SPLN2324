
**Introdução**

Explicação da abordagem para resolução do TPC3.

**Informações**
* Nome: Gonçalo Campos Pereira
* Número: pg53834

**Problema**

Programa para automatização da criação de ficheiros *toml*.

**Solução**
* Através do módulo *glob* obtém-se aquele que será o campo "nome" no ficheiro final.
* Os campos "autor" e "email" encontram-se num ficheiro (*metadata.json*) localizado na *home* do dispositivo.
* Por último, é utilziado o terminal para se obter as dependências que serão utilizadas. Para isso, o programa pede ao utlizador o número de dependências que vai ter e, de seguida, os seus nomes, um a um.
* É utilizado também o módulo *jinja* e, através do seu método *Template* é feita a intrepolação das variáveis na string final. Para isto, usa-se também o método *render*, do mesmo módulo.
* O redirecionamento da string final para o ficheiro é feito passando o nome do ficheiro pretendido como argumento no terminal.

O programa executa através da invocação do seguinte comando:
    
    python3 makepyproject.py <ficheiro_output>
