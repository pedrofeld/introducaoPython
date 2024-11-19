"""
Utilitários python para auxiliar na programação.

dir -> Apresenta todos os atributos/propriedades e funções/métodos disponíveis para determinado tipo de dado ou variável.

dir(tipo de dado/variável)

help -> Apresenta a documentação/como utilizar os atributos/propriedades e funções/métodos disponíveis para
determinado tipo de dado ou variável.

help(tipo de dado/variável.propriedade)

-------------

Por exemplo:

python - vai iniciar os comandos no próprio terminal

dir("pedro") - vai mostrar todos os métodos e funções disponíveis para essa variável string
help("pedro".upper) - vai mostrar como usar o método "upper" com a variável string

dir(5) - vai mostrar todos os métodos e funções disponíveis para essa variável number
num = 5 - define a variável como number
help(num.__add__) - vai mostrar como usar o método "add" com a variável number

CLICLAR "Q" PARA SAIR DO HELP

"""

print(dir('pedro'))