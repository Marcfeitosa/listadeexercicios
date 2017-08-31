from random import choice, randint
from time import sleep

cores = {'limpa': '\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'roxo':'\033[35m',
         'azulclaro':'\033[36m',
         'cinza':'\033[37m'}

print("""Desafio 028
Escreva um programa que faça o computador em um número inteiro entre 0 e 5 e 
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador:

O programa deverá escrever na tela se o usuário venceu ou perdeu.""")

print('Eu vou pensar em um número entre 0 e 5, você consegue descobrir qual é o número?')
cpu = [0, 1, 2, 3, 4, 5]
m = choice(cpu)
tu = int(input('Digite o número no qual eu pensei: '))
print('Parabéns, você acertou.' if m == tu else 'você errou meu camarada, o número que eu escolhi é o {}{}{}.'
      .format(cores['amarelo'],m,cores['limpa']))

com = randint(0, 5) #makes the computer think
print(cores['vermelho'],'-=-' * 20,cores['limpa'])
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print(cores['vermelho'],'-=-' * 20,cores['limpa'])
player = int(input('Em que número eu pensei? '))#player guess
print('PROCESSING')
sleep(2)
if player == com:
    print('Parabéns, você venceu.')
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(com, player))