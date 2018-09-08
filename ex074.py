"""Desafio 074

Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla."""

from random import randint

n1 = randint(0, 9999)
n2 = randint(0, 9999)
n3 = randint(0, 9999)
n4 = randint(0, 9999)
n5 = randint(0, 9999)

print(f'Os números escolhidos aleatoriamente são: {n1}, {n2}, {n3}, {n4}, {n5}. ')

numerosgerados = (n1, n2, n3, n4, n5)
print(sorted(numerosgerados))
print(numerosgerados[0])
print(numerosgerados[-1])

numerosgerados2 = (randint(0, 9999), randint(0, 9999), randint(0, 9999), randint(0, 9999), randint(0, 9999))
print(f'Os númmeros gerados foram: {numerosgerados2}. ')
print(f'\nO maior valor sorteado foi {max(numerosgerados2)}')
print(f'\nO menor valor sorteado foi {min(numerosgerados2)}')
