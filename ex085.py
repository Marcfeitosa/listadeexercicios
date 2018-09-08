"""Desafio 85
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valoes pares e ímpares. No final, mostre os valores pares e impares em ordem crescente."""

lista =[[], []]
for i in range(0, 7):
    x = int(input('Digite um número: '))
    if x % 2 == 0:
        lista[0].append(x)
    else:
        lista[1].append(x)
print(lista)
pares = lista[0]
pares.sort()
print(pares)
impares = lista[1]
impares.sort()
print(impares)
