"""Exercpicio 55

Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos"""
maior = 0
menor = 0
for i in range(0, 5):
    peso = int(input('Qual é o peso da {}ª pessoa? '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O menor peso lido é {} e o maior peso lido é {}.'.format(menor, maior))