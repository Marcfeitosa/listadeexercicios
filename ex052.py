"""Exercício 52

Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

x = int(input('Número que precisamos verificar se é primo: '))
primochecker = (2, 3, 5, 7, x)
totaldedivisoes = 0
for i in range(1,x+1):
    if x % i == 0:
        print('\033[34m', end='')
        totaldedivisoes += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
print('\n\033[mO número {} foi divisível {} vezes.'.format(x,totaldedivisoes))
if totaldedivisoes == 2:
    print('Ele é primo.'.format(x), end='')
else:
    print('Ele nao é primo.'.format(x), end='')