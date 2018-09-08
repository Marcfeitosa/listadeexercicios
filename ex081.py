"""Exercício 81
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:

A) Quantos números foram digitados.

B) A lista de valores, ordenada de forma decrescente.

C) Se o valor 5 foi digitado e está ou não na lista.

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
print(f'{len(lista)} valores foram gerados.')
lista.sort(reverse=True)
print(f'A lista de valores foi {lista}')
if 5 in lista:
    print('O nº 5 foi digitado')
else:
    print('O nº 5 não foi digitado')
