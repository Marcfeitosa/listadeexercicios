"""Desafio 058
Melhore o jogo do DESAFIO 028 onde o computador vai pensar em um número de 0 a 10. Sò que agora
o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer"""

from random import choice, randint
from time import sleep

cores = {'limpa': '\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'roxo':'\033[35m',
         'azulclaro':'\033[36m',
         'cinza':'\033[37m'}

"""Desafio 028
Escreva um programa que faça o computador em um número inteiro entre 0 e 5 e 
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador:
O programa deverá escrever na tela se o usuário venceu ou perdeu."""

print('Eu vou pensar em um número entre 0 e 10, você consegue descobrir qual é o número?')
cpu = randint(0, 10)
m = choice(cpu)
tu = int(input('Digite o número no qual eu pensei: '))
print('Processando')
sleep(0.5)
countr = 0
while m != tu:
    tu = int(input('você errou meu camarada, nao foi esse o número que eu escolhi, tente de novo:'))
    countr += 1
if countr == 1:
    print('Poxa, você precisou de {} tentativas até acertar.'.format(countr))
else:
    print('é meu velho, você precisou de {} tentativas até acertar.'.format(countr))
#print('Parabéns, você acertou.' if m == tu else 'você errou meu camarada, nao foi esse o número que eu escolhi')

com = randint(0, 10) #makes the computer think
print(cores['vermelho'],'-=-' * 20,cores['limpa'])
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print(cores['vermelho'],'-=-' * 20,cores['limpa'])
player = int(input('Em que número eu pensei? '))#player guess
print('PROCESSING')
sleep(0.5)
while player != com:
    player = int(input('você errou meu camarada, nao foi esse o número que eu escolhi, tente de novo:'))
    countr += 1
if countr == 1:
    print('Poxa, você precisou de {} tentativas até acertar.'.format(countr))
else:
    print('é meu velho, você precisou de {} tentativas até acertar.'.format(countr))

computador = randint(0, 10)
print('Em qual número eu pensei?')
print('adv')