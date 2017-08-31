print("""Desafio 31
Escreva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando
R$ 0,50 por KM para viagens de até 200Km e R$ 0,45 para viagens mais longas.""")
dist = float(input('Qual é a distância a ser percorrida? '))
if dist > 200:
    print('O preço da passagem será de R$\033[4;35m{:2f}\033[m.'.format(float(dist * 0.45)))
else:
    print("O preço da passagem será de R$\033[4;36m{:2f}\033[m.".format(float(dist * 0.50)))