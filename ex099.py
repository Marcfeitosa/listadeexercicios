cores = {'limpa': '\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'roxo':'\033[35m',
         'azulclaro':'\033[36m',
         'cinza':'\033[37m'}

print("""Desafio 099
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
e realize a contagem

Seu programa tem que analisar todos os valores e dizer qual deles é o maior

""")

from time import sleep

def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados... ')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado froi {maior}.')
    


# programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
