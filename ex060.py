"""DESAFIO 060
Faça um programa que leia um núemro qualquer e mostre o seu fatorial

Ex:
5! = 5x4x3x2x1=120"""

from math import factorial

cores = {'limpa': '\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'roxo':'\033[35m',
         'azulclaro':'\033[36m',
         'cinza':'\033[37m'}

n = int(input('Escolha um número para fatorarmos: '))
print(cores['azul'],n,'! =',cores['limpa'],end='')
print(n,end='')
f = factorial(n)
while n-1 != 0:
    n -= 1
    print(' x {}'.format(n),end='')
print(' =',cores['vermelho'],f,cores['limpa'])

print(cores['amarelo'],'-=-' * 20,cores['limpa'])
n = int(input('Escolha um número para fatorarmos: '))
c = n
print(cores['azul'],'{}! ='.format(n),cores['limpa'],end='')
print(n,'x ',end='')
while c >= 2:
    c -= 1
    print('{} '.format(c),end='')
    print('x ' if c > 1 else '=', end='')
print(cores['vermelho'],factorial(n),cores['limpa'])

print(cores['amarelo'],'-=-' * 20,cores['limpa'])
n = int(input('Escolha um número para fatorarmos: '))
c = n
f = 1
print(cores['azul'],'{}! ='.format(n),cores['limpa'],end='')
print(n,'x ',end='')
while c >= 2:
    f *= c
    c -= 1
    print('{} '.format(c), end='')
    print('x ' if c > 1 else '=', end='')
print(cores['vermelho'],f,cores['limpa'])

print(cores['amarelo'],'-=-' * 20,cores['limpa'])
n = int(input('Escolha um número para fatorarmos: '))
print(cores['azul'],'{}! ='.format(n),cores['limpa'],end='')
f = 1
for n in range(n, 0, -1):
    f *= n
    print('{} '.format(n), end='')
    print('x ' if n > 1 else '=', end='')
print(cores['vermelho'],f,cores['limpa'])

print('Tudo fatorado')