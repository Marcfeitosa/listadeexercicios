cores = {'limpa': '\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'roxo':'\033[35m',
         'azulclaro':'\033[36m',
         'cinza':'\033[37m'}

print("""Desafio 100
Faça um programa que tenha uma lista chamada numeros() e 2 funções chamadas sorteia() e somapar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e
a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.""")

from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0,5):
        x = randint(0,100)
        lista.append(x)
        print(f'{x} ', end='', flush=True)
        sleep(0.5)
    print('PRONTO!')

def somapar(lista):
    soma = 0
    for x in lista:
        if x % 2 == 0:
            soma += x
    print(f'Somando os valores pares de {lista}, temos {soma}')

numeros = list()
sorteia(numeros)
somapar(numeros)