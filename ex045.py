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
    if jogadacpu == cpu[0] and jjogador == jogador[2]:
        print(emojify(jogador[jjogador]), ' Você Ganhou!!!')
    elif jogadacpu == cpu[0] and jjogador == jogador[0]:
        print(emojify(jogador[jjogador]), ' Jogo empatado mané')
    elif jogadacpu == cpu[0] and jjogador == jogador[1]:
        print(emojify(jogador[jjogador]), ' Você perdeu mané')
    elif jogadacpu == cpu[0] and jjogador == jogador[4]:
        print(emojify(jogador[jjogador]), ' Você é do METAAAAAAALLL, VOCÊ GANHOU FERA!!!!')
    elif jogadacpu == cpu[1] and jjogador == jogador[0]:
        print(emojify(jogador[jjogador]), ' Você Ganhou!!!')
    elif jogadacpu == cpu[1] and jjogador == jogador[1]:
        print(emojify(jogador[jjogador]), ' Jogo empatado mané')
    elif jogadacpu == cpu[1] and jjogador == jogador[2]:
        print(emojify(jogador[jjogador]), ' Você perdeu mané')
    elif jogadacpu == cpu[1] and jjogador == jogador[4]:
        print(emojify(jogador[jjogador]), ' Você é do METAAAAAAALLL, VOCÊ GANHOU FERA!!!!')
    elif jogadacpu == cpu[2] and jjogador == jogador[0]:
        print(emojify(jogador[jjogador]), ' Você perdeu mané')
    elif jogadacpu == cpu[2] and jjogador == jogador[1]:
        print(emojify(jogador[jjogador]), ' Você Ganhou!!!')
    elif jogadacpu == cpu[2] and jjogador == jogador[2]:
        print(emojify(jogador[jjogador]), ' Jogo empatado mané')
    elif jogadacpu == cpu[2] and jjogador == jogador[4]:
        print(emojify(jogador[jjogador]), ' Você é do METAAAAAAALLL, VOCÊ GANHOU FERA!!!!')
    else:
        print(' TU NÃO SABE LER O ANTA???? DIGITA SÓ AS OPÇÕES QUE EU TE DEI... BURRO!!!!')