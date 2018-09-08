"""Desafio 72

Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.

Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""

tupladecontagemate20 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
                        'treze', 'quatorze ou catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
continuar = ''
while True:
    while True:
        numerodigitado = int(input('Digite um número entre 0 e 20 para verificação: '))
        if 0 <= numerodigitado <=20:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou \033[36m{tupladecontagemate20[numerodigitado]}.\033[m')
    print('~' * 20)
    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Entrada inválida, tente novamente. '))
    if continuar == 'N':
        break
