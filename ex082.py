"""Exercício 82
Crie um programa que vai ler vários números e coloca-los em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""
lista = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    print('valor adicionado com sucesso.')
    r = str(input('Quer continuar? [S/N}'))
    if r in "Nn":
        print()
        break

print(lista)
print('-='*30)
pares = []
impares = []

for i in lista:
    x = i % 2
    if x == 0:
        pares.append(i)
    else:
        impares.append(i)

print(pares)
print('-='*30)
print(impares)
