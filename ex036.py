print("""Desafio 36

Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.""")

housevalue = float(input('Qual e o valor do imovel?'))
salary = float(input('Qual é o seu salário?'))
term = int(input('Em quantos anos você vai pagar?'))*12
parcel = housevalue/term
if parcel > salary*0.30:
    print("este financiamento não é possível: ")
else:
    print('O seu financiamento será de {}'.format(parcel))

print (3*'===============xx==============xx' + '==============')