"""Exercício 48

Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se
encontram no intervalo entre 1 a 500"""

s=0
cont=0
for i in range(1,501,2):
    if i % 3 == 0:
        cont += 1
        s += i
print("O somatórtio de todos os {} números ímpares de 0 a 500 é {}.".format(cont,s))
