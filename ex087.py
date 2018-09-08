"""Desafio 87
Aprimore o Desafio anterior (86), mostrando no final:

A) A soma de todos os valores paress digitados.

B) A soma dos valores da terceira coluna.

C) O maior valor da segunda linha."""

import numpy

matriz = []
temp = []
somapares1 = 0
maior = 0
for i in range(0, 3):
    for j in range(0, 3):
        j = int(input(f'Digite um número para a {i+1}ª linha e {j+1}ª coluna '))
        temp.append(j)
    matriz.append(temp[:])
    temp.clear()

print("x"*40)
print(numpy.matrix(matriz))
print('x'*40)
print()

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]',end='')
        if matriz[i][j] % 2 == 0:
            somapares1 += matriz[i][j]
    print()
print()
print('x'*40)
print()
print(f'A soma dos números pares no modelo Guanabara {somapares1}')

print()

somapares = 0
for i in matriz:
    for j in i:
        if j % 2 == 0:
            somapares += j
print(f'a soma dos números pares no modelo Márcio {somapares}')

print()
print('x'*40)
print()

soma3coluna = 0
for linha in range(0, 3):
    soma3coluna += matriz[linha][2]
print(f'soma da 3ª coluna no modelo Guanabara {soma3coluna}')

print()
print('x'*40)
print()

print(f'o maior número da 2ª linha no modelo Márcio {numpy.max(matriz[1])}')
print()
for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f'o maior número da 2ª linha no modelo Guanabara {maior}')
