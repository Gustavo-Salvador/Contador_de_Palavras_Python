# Como o projeto funciona

## Bibliotecas

### unicodedata.normalize

Utilizada para remover os caracteres especiais

### pprint

Utilizada para printar objetos de forma mais legivel

### operator

Utilizada para definir como o dicionário será organizando 

## Cabeçalho/inicio

O Progama possui 4 variáveis pré definidas:
 - Texto: utilizada para armazenar o texto não formatado;
 - TextoForm: utilizada para armazenar o texto formatado;
 - Priv: Que embora signifique "privilégio", na verdade é o grau de acesso que o usuário tem a aplicação (ou seja, um privilégio 2 da acesso as funções com privilégio <= 2)
 - Opc: Define as funções e textos do menu através da seguinte estrutura: *'(nome da função a ser chamada)': [(privilégio minimo para usar a função), (número da opção no menu), '(texto que aparecera no menu)']*

## Funções

### openFile

Abre o arquivo .txt desejado

### printTexto

Printa o texto obtido na abertura do arquivo

### limpaTexto

substitui os caracteres especiais por caracteres padrões, por exemplo: 'ç' => 'c', 'á' => 'a'...

### printTextoForm

Printa o texto sem caracteres especiais

### contaPalavras

conta as aparições de cada palavra do texto guardando isso em um dicionário, também conhecido como hash

### printContagem

Printa a quantidade de vezes que cada palavra apareceu

### query

Permite fazer buscas da quantidade de vezes que certa palavra apareceu, permite busca de multiplas palavras separadas por ','

### printExtremos

Printa a(s) palavra(s) que apareceu(eram) mais e menos vezes

### sair

Encerra execução do programa

## menu

Permite executar as funções cadastradas na variável 'opc' digitando o código de chamada da mesma, vale citar que só aparecerão as funções que são possiveis executar no momento

