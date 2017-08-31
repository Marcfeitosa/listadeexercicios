print("""Desafio 30
Escreva um programa que diga se um número é par ou impar""")
x = float(input('Escreva um número: \033[34m \033[m'))
if x % 2 != 0:
    print('Número impar')
else:
    print('Número par')