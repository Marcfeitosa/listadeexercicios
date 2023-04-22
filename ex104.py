"""
Desafio 104:

Crie um programa que tenha uma função LeiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico

ex:
n=LeiaInt('Digite um n')

"""

def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return print(f'Você digitou: {n}')

#programa principal
n = LeiaInt('Digite um número inteiro: ')
