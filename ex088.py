"""Desafio 88
Faça um programa que ajude um jogador de MEGA SENA a criar palpites. O programa vai perguntar quantos jogos
serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta."""

from random import sample
from time import sleep

print('-'*40)
print('          JOGO NA MEGA SENA')
print('-'*40)
print()
n = int(input('quantos jogos da mega-sena deseja fazer? '))
listacompleta = []
for i in range(n):
    jogo = sample(range(0, 61), 6)
    listacompleta.append(jogo)
print()
print(f'-=-=-= SORTEANDO {n} JOGOS -=-=-=')

for i, j in enumerate(listacompleta):
    sleep(1)
    print(f'Jogo {i+1}: {j}')
print('-=-=-= BOA SORTE -=-=-=')

