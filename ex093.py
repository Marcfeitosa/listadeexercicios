"""Exercício 093

Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas
partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um
dicionário, incluindo total de gols feitos durante um campeonato."""

jogador = {}
jogador['nome'] = str(input('Qual é o nome do seu jogador: '))
jogador['partidas disputadas'] = int(input('Quantas partidas ele disputou: '))
jogador['gols por partida'] = int(input('quantos gols por partida: '))
jogador['gols no campeonato'] = jogador['partidas disputadas'] * jogador['gols por partida']
print()
print('=+' * 30)
print()
for i, j in jogador.items():
    print(f'{i} = {j}')
