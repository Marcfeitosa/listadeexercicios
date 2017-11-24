"""DESAFIO 42

Refaça o DESAFIO 35 dos triangulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

- EQUILATÉRO: todos os lados iguais

- ISÓSCELES: dois lados iguais

- ESCALENO: todos os lados diferentes"""

r1 = float(input('Comprimento da reta 1: '))
r2 = float(input('Comprimento da reta 2: '))
r3 = float(input('Comprimento da reta 3: '))
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('os segmentos de reta acima podem formar um triângulo ', end='')
    if r1 == r2 and r2 == r3:
        print("EQUILÁTERO")
    elif r1 == r2 and r2 != r3 or r1 == r3:
        print("ISÓSCELES")
    else:
        print("ESCALENO")
else:
    print('Os segmentos acima nao formam um triângulo ', end='')
    if r1 == r2 == r3:
        print("EQUILÁTERO")
    elif r1 != r2 != r3 != r1:
        print("ESCALENO")
    else:
        print("ISÓSCELES")