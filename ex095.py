"""Exercício 095

Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualizações de detalhes do
aproveitamento de cada jogador."""

time = []
jogador = {}
while True:
    jogador['nome'] = str(input('Qual é o nome do seu jogador: '))
    jogador['partidas disputadas'] = int(input('Quantas partidas ele disputou: '))
    jogador['gols por partida'] = int(input('quantos gols por partida: '))
    jogador['gols no campeonato'] = jogador['partidas disputadas'] * jogador['gols por partida']
    time.append(jogador.copy())
    print('=+'*30)
    continua = str(input('Quer cadastrar um outro jogador? '))
    if continua not in 'Nn':
        print('=+'*40)
    else:
        break
print()
print('=+' * 30)
print()
for a in time:
    for i, j in a.items():
        print(f'{i} = {j}')
    print('~~' * 30)