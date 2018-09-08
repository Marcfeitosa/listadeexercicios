"""Desafio 86
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
no final, mostre a matriz na tela, com a formatação correta."""

import numpy

matriz = []
temp = []
for i in range(0, 3):
    for j in range(0, 3):
        j = int(input(f'Digite um número para a {i+1}ª linha e {j+1}ª coluna '))
        temp.append(j)
    matriz.append(temp[:])
    temp.clear()
print(numpy.matrix(matriz))
print()
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]',end='')
    print()
