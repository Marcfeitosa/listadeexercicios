print("""Exercício 024
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com 'Santo'""")

cidade = input('Digite o nome da cidade que deseja conferir: ').strip().title()
lista_cidade = cidade.split()
if lista_cidade[0] == 'Santo':
    print('A cidade começa com o nome Santo.')
else:
    print('A cidade não começa com Santo.')
