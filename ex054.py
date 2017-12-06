"""Exercpicio 54

Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas ja são maiores"""

import datetime
today = datetime.date.today()
cont = 0
contagemaiores = 0
contagemenores = 0
for i in range(0,7):
    cont += 1
    x=int(input('em que ano a {}ª pessoa nasceu? '.format(cont)))
    if today.year - x >= 18:
        z=print('A {}ª pessoa já é maior de idade.'.format(cont))
        contagemaiores += 1
    else:
        y=print('A {}ª não é maior de idade.'.format(cont))
        contagemenores += 1
print('Existem {} maiores de idade nesse grupo.'.format(contagemaiores))
print('Existem {} menores de idade nesse grupo'.format(contagemenores))