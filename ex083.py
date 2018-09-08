"""Exercício 83
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se
a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""

expressao = str(input('Digite uma expressão: '))
stack = []
open, close = '(', ')'
for i in expressao:
    if i in open:
        stack.append(i)
    if i in close:
        stack.append(i)
for pos, j in enumerate(stack):
    if (pos % 2 == 0) and (j == '(' or pos % 2 != 0) and (j == ')'):
        print('Expressão OK')
    else:
        print(f'A expressão está errada na {pos+1}ª posição.')

expressao2 = str(input('Digite uma expressão: '))
stack2 = []
for parenteses in expressao:
    if parenteses == '(':
        stack2.append('(')
    elif parenteses == ')':
        if len(stack2) > 0:
            stack2.pop()
        else:
            stack2.append(')')
            break
if len(stack2) == 0:
    print('Sua expressão está correta')
else:
    print('Sua expressão não está correta')

expressão = input('Digite a expressão: ')
lista = []
for i in range(0, len(expressão)):
    lista.append(expressão[i])

if lista.count('(') == lista.count(')'):
    print('A expressão é válida!')
else:
    print('Sua expressão está errada!')﻿


