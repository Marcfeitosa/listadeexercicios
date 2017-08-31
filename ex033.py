print("""Desafio 33
Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor""")
f = int(input('Digite o primeiro número: '))
g = int(input('Digite o segundo número: '))
h = int(input('Digite o terceiro número: '))
list_sort = [f, g, h]
print('O menor número é \033[4;31m{}\033[m.'.format(min(list_sort)))
print('O maior número é \033[4;33m{}\033[m.'.format(max(list_sort)))

print("""Segunda solução possível""")
menor = f
if g<f and g<h:
    menor = g
if h<f and h<g:
    menor = h
maior = f
if g>f and g>h:
    maior = g
if h>f and h>g:
    maior = h
print("O menor número digitado foi o {}.".format(menor))
print("O maior número digitado foi o {}.".format(maior))