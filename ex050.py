"""Exercício 50

Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o"""
s = 0
c = 0
for i in range(0,8):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        s += n
        c += 1
print('A soma de todos os {} números pares é igual a {}.'.format(c,s))