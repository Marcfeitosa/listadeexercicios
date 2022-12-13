print("""Desafio 096
Faça um programa que tenha uma função chamada área(), que receba as dimensões
de um terreno retangular (largura e comprimento) e mostre a área do terreno.""")

def area(largura, comprimento):
    a = largura * comprimento
    return print(f'A área de um terreno {largura} x {comprimento} é de {a}m².')

#Programa prnicipal
print('Controle de Terrenos')
print('-' * 20)
largura = float(input('Qual é a largura do terreno: '))
comprimento = float(input('Qual é o comprimento do terreno: '))
area(largura, comprimento)
