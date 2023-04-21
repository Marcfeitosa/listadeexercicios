"""
Desafio 103:

 Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
 O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha seido informado corretamente.

"""

def ficha(nome='', gols=0):
    if nome == '':
        nome = '<desconhecido>'
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

nome = input('Nome do jogador: ')
gols = input('Número de gols: ')

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

ficha(nome, gols)
