print("""Desafio 35
Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo""")
print('\033[1;31m-=-\033[m' * 20)
print('Analisador de triângulos')
print('\033[1;31m-=-\033[m' * 20)

r1 = float(input('Comprimento da reta 1: '))
r2 = float(input('Comprimento da reta 2: '))
r3 = float(input('Comprimento da reta 3: '))
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('os segmentos de reta acima podem formar um triângulo')
else:
    print('Os segmentos acima nao formam um triângulo')