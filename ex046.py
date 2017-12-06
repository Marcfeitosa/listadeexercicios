"""Exercíio 46

Faça um programa que mostre na tela uma contagem regressiva para os fogos de artifício.
Indo de 10 até 0, com uma pausa de um segundo entre eles."""

from pyemojify import emojify
from time import sleep

for c in range(10,0,-1):
    emoj = emojify(":sparkles:")
    print(c, emoj)
    sleep(1)
print (emoj*10)
print("FELIZ ANO NOVO!!!!!!!")
