"""Exercício 78
Faça um programa que leia 5 valores númericos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista."""

lista = []
for i in range(0,5,1):
    y = int(input(f'Digite {i+1}° número: '))
    lista.append(y)
print(f'Minha lista é {lista}')
print(f'o menor número é {min(lista)} na {lista.index(min(lista))}ª posição e o maior é {max(lista)} na posição {lista.index(max(lista))}')
for c, p in enumerate(lista):
    if p == max(lista):
        print(c)

print()
print('-='*30)
print()

valores = []
maior=0
menor=0
for ent in range(0,5):
    valores.append(int(input(f'digite um valor para a posição {ent}: ')))
    if ent == 0:
        maior = menor = valores[ent]
    else:
        if valores[ent] > maior:
            maior = valores[ent]
        if valores[ent] < menor:
            menor = valores[ent]
print('-='*30)
print(f'Minha lista é {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...',end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...',end='')
