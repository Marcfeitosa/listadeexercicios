print('Exercício 016')
from math import floor, ceil, trunc

def arrend(numero):
    if num2 - floor(num2) < 0.5:
        numero = floor(num2)
        return numero
    else: return ceil(num2)
num2 = float(input("digite um número não inteiro: "))
print("o número inteiro correspondente é: {}".format(arrend(num2)))
print('A parte interia do número digitado, usando o "truncate, é {}'.format(trunc(num2)))
print('A parte interia do número digitado "usando o int" é {}'.format(int(num2)))