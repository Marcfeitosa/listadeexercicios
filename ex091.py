"""Exercício 091

Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dados."""

from random import randint
from time import sleep
from operator import itemgetter

jogadas = {}
jogadores = []

for i in range(0, 4):
    jogadas['jogador'] = str(f'Jogador {i+1}')
    jogadas['dado'] = int(f'{randint(1, 6)}')
    sleep(1)
    print(f'O jogador {jogadas["jogador"]} tirou {jogadas["dado"]}')
    jogadores.append(jogadas.copy())
print('Ranking dos jogadores')
listarankeada = sorted(jogadores, key=itemgetter('dado'), reverse=True)
for pos, j in enumerate(listarankeada):
    sleep(1)
    print(f'{pos+1}º lugar: jogador {j["jogador"]} com {j["dado"]}')

print()
print('=-'*40)
print()


"""Solução Guanabara"""
jogo = {'jogador 1' : randint(1, 6),
        'jogador 2' : randint(1, 6),
        'jogador 3' : randint(1, 6),
        'jogador 4' : randint(1, 6)}
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}.')
    sleep(1)