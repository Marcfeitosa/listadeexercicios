print (3*'===============xx==============xx' + '==============')

"""DESAFIO 37

Escreva um programa que leia um número inteiro qualquer 
e peça para o usuário escolher qual será a base de conversão:

-1 para binário
-2 para octal
-3 para hexadecimal"""

import types

def checkifnumeric( num ):
    while True:
        if num < 400:
            choice = int(input("""Para qual base você deseja converter
                            -1 para binário
                            -2 para octal
                            -3 para hexadecimal"""))
            return calc(num,choice)
        else:
            print('Digita um número sua anta...')
            break


def calc(num,choice):
    if choice <= 3:
            if choice == 1:
                print('O número {} em binário é {}'.format(num, bin(num)))
            elif choice == 2:
                print('O número {} em octal é {}.'.format(num, oct(num)))
            elif choice == 3:
                print('O número {} em hexadecimal é {}'.format(num, hex(num)))
            else:
                print('Opção inválida')
    else:
        print('número inválido')
        choice = int("""Para qual base você deseja converter
                            -1 para binário
                            -2 para octal
                            -3 para hexadecimal""")

    print (3*'===============xx==============xx' + '==============')
number = int(input('Excolha um número qualquer: '))

checkifnumeric(number)
