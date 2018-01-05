"""Desafio 068

Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""

from random import randint

cores = {'limpa': '\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'roxo':'\033[35m',
         'azulclaro':'\033[36m',
         'cinza':'\033[37m'}

cpu = randint(0, 11)
n = contv = contd = 0
escolha = ' '
while contd <= 0:
    n = int(input('Digite um número para batermos par ou impar: '))
    while escolha not in 'PI':
        escolha = str(input('Vou ganhar... você quer par ou impar? [I/P] ')).upper().strip()[0]
    cpu = randint(0, 11)
    magic = ((cpu + n) % 2)
    print(f'O computador jogou {cpu}')
    if escolha == 'I' and magic == 0:
        print(cores['azulclaro'],'PERDEU... HAAAAA, deu PAR',cores['limpa'])
        contd += 1
    elif escolha == 'P' and magic == 0:
        print(cores['vermelho'],'ganhou, de par... VAMOS MAIS UMA...',cores['limpa'])
        contv += 1
    elif escolha == 'I' and magic == 1:
        print(cores['vermelho'], 'ganhou, deu ímpar... VAMOS MAIS UMA...', cores['limpa'])
        contv += 1
    elif escolha == 'P' and magic == 1:
        print(cores['azulclaro'], 'PERDEU, de ÍMPAR... HAAAAA', cores['limpa'])
        contd += 1
if contv >= 3:
    print(cores['amarelo'],f'Poxa, foi difícil ganhar de você, {contv} vitórias seguidas',cores['limpa'])
else:
    print(cores['azul'],'Molezinha ganhar de você',cores['limpa'])