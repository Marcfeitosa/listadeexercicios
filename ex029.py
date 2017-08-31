print("""Desafio 029
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.""")

cores = {'limpa': '\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'roxo':'\033[35m',
         'azulclaro':'\033[36m',
         'cinza':'\033[37m'}

vel = float(input('qual é a velocidade do carro? '))
print('cinza-=-limpa' * 20)
print('Multado, a multa vai custar {}{}{}'.format(cores['vermelhor'],(vel - 80.00) * 7,cores['limpa']) if vel > 80.00 else 'continue assim.')

if vel > 80:
    print('multado - valor a pagar: R$ {}{}{}.'.format(cores['vermelho'],(vel-80)*7),cores['limpa'])
print('Tenha um bom dia, dirija com segurança.')