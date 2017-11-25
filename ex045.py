"""DESAFIO 045

Crie um programa que faça o computador jogar Jokenpô com você"""

from random import randint
from pyemojify import emojify
from time import sleep
cpu = [":hand:", ":punch:", ":v:"]
jogador = [":hand:", ":punch:", ":v:", ":metal:"]
jogadacpu = randint(0, 2)
jjogador = int(input(emojify('''escolha uma opção:
                                        0 - :hand:
                                        1 - :punch:
                                        2 - :v: 
                                        ''')))
print("Você jogou: ", emojify(jogador[jjogador]))
sleep(1)
print("JO")
sleep(1)
print("   KEN")
sleep(1)
print("       PO")
sleep(1)
print()
print('CPU Jogou: ')
print(emojify(cpu[jogadacpu]))
if jogadacpu == 0 and jjogador == 2:
    print(' Você Ganhou!!!')
elif jogadacpu == 0 and jjogador == 0:
    print(' Jogo empatado mané')
elif jogadacpu == 0 and jjogador == 1:
    print(' Você perdeu mané')
elif jogadacpu == 0 and jjogador == 4:
    print(' Você é do METAAAAAAALLL, VOCÊ GANHOU FERA!!!!')
elif jogadacpu == 1 and jjogador == 0:
    print(' Você Ganhou!!!')
elif jogadacpu == 1 and jjogador == 1:
    print(' Jogo empatado mané')
elif jogadacpu == 1 and jjogador == 2:
    print(' Você perdeu mané')
elif jogadacpu == 1 and jjogador == 4:
    print(' Você é do METAAAAAAALLL, VOCÊ GANHOU FERA!!!!')
elif jogadacpu == 2 and jjogador == 0:
    print(' Você perdeu mané')
elif jogadacpu == 2 and jjogador == 1:
    print(' Você Ganhou!!!')
elif jogadacpu == 2 and jjogador == 2:
    print(' Jogo empatado mané')
elif jogadacpu == 2 and jjogador == 4:
    print(' Você é do METAAAAAAALLL, VOCÊ GANHOU FERA!!!!')
else:
    print(' TU NÃO SABE LER O ANTA???? DIGITA SÓ AS OPÇÕES QUE EU TE DEI... BURRO!!!!')
