""""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo string

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Angelina Jolie'
- Aspas duplas -> "Angelina Jolie"
- Aspas simples triplas -> '''Angelina Jolie'''
"""
# - Aspas duplas triplas -> """Angelina Jolie"""

# Entrada de dados

# print("Qual seu nome?")
# nome = input() # input = entrada

nome = input('Qual seu nome?')

# Exemplo de print 'antigo'
print('Seja bem-vindo(a) %s' % nome)

# Exemplo de print 'novo'
print('Seja bem-vindo(a) {0}'.format(nome))

# Exemplo de print 'mais atual'
print(f'Seja bem-vindo(a) {nome}')

# print("Qual sua idade?")
# idade = input()

idade = int(input('Qual sua idade?'))

# Saída

# Exemplo de print antigo
print("%s tem %s anos" % (nome, idade))

# Exemplo de print novo
print('{0} tem {1} anos'.format(nome, idade))

# Exemplo de print 'mais atual'
print(f'{nome} tem {idade} anos')

"""
# int(idade) => cast

Cast é a "conversão" de um tipo de dado para outro
"""

print(f'{nome} nasceu em {2024 - idade}')

# print(f'{nome} nasceu em {2024 - int(idade)}')