"""Desafio 070

Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000,00
C) Qual é o nome do produto mais barato."""

print('-'*40)
print('LOJAS BARATÃO')
print('-'*40)

biscoito = 2.50
leite = 2.00
maçã_kg = 2.5
pêra_kg = 2.4
desinfetante = 5.6
sabãoempó = 8.50
sabonete = 1.46
papelhigiênico = 9.2
carne_kg = 10.60
achocolatado = 7.52
frango_kg = 8.91
verdura_kg = 3.51
águacomgás = 1.48
lapiseira = 2.00

somaproduto = somaquantidade = cont1000 = maior = menor = somavalor = cont = 0
barato = ''
while True:
    produto = str(input('Digite o produto; '))
    quantidade = int(input('Unidades: '))
    preço = float(input('Preço: R$ '))
    cont += 1
    total = preço*quantidade
    somaproduto += 1
    somaquantidade += quantidade
    somavalor += total
    print(f'Total Parcial R$ {somavalor}')
    if preço > 1000:
        cont1000 += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    próximo = ' '
    while próximo not in 'SN':
        próximo = str(input('Tem róximo produto? [S/N] ')).upper().strip()[0]
        print('~'*10)
    if próximo == 'N':
        break
print('~'*40)
print(f'você comprou uma variedade de {somaproduto} produtos.')
print(f'Adquiristes um total de {somaquantidade} unidades de produto.')
print(f'Sua compra foi de R$ {somavalor}.')
print(f'O produto mais barato foi {barato} que adquiristes custou R$ {menor}')
print('{:-^40}'.format('FIM DO PROGRAMA'))
