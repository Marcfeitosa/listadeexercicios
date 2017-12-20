"""DESAGIO 059
Crie um programa que cria dois valores e coloque o menu na tela:

[1]SOMAR
[2]MULTIPLICAR
[3]MAIOR
[4]NOVOS NÚMEROS
[5]SAIR DO PROGRAMA

Seu programa deverá deverá realizar a operação solicitada em cada caso."""

from random import randint
from time import sleep

cores = {'limpa': '\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'roxo':'\033[35m',
         'azulclaro':'\033[36m',
         'cinza':'\033[37m'}

n1 = randint(0, 9999)
n2 = randint(0, 9999)
print('O 1º número que o computador escolheu foi {}.'.format(n1))
print('O 2º número que o computador escolhei foi {}.'.format(n2))
print('Processing... ')
sleep(1)
choice = 0
while choice != 5:
    print("""
[ 1 ]SOMAR
[ 2 ]MULTIPLICAR
[ 3 ]MAIOR
[ 4 ]NOVOS NÚMEROS
[ 5 ]SAIR DO PROGRAMA
    """)
    choice = int(input())
    #while choice not in (1, 2, 3, 4, 5):
        #choice = int(input('Não é uma opção válida, tente de novo: '))
    if choice == 1:
        print('A soma de {} e {} é {}.'.format(n1, n2, (n1 + n2)))
    elif choice == 2:
        print('A multiplicação de {} por {} é {}.'.format(n1, n2, (n1 * n2)))
    elif choice == 3:
        if n1 > n2:
            print('O maior número é {}.'.format(n1))
        else:
            print('O maior número é {}'.format(n2))
    elif choice == 4:
        n3 = randint(0, 9999)
        n4 = randint(0, 9999)
        print('O novo 1º número que o computador escolheu foi {}.'.format(n3))
        print('O novo 2º número que o computador escolhei foi {}.'.format(n4))
    elif choice == 5:
        print("C'est la fin")
    else:
        int(input("""Não é uma opção válida, tente de novo: 
        [ 1 ]SOMAR
        [ 2 ]MULTIPLICAR
        [ 3 ]MAIOR
        [ 4 ]NOVOS NÚMEROS
        [ 5 ]SAIR DO PROGRAMA
"""))