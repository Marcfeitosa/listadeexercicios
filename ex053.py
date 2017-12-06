"""Exercício 53

Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços."""

tocheck = str(input('Digite uma frase: ')).strip().upper()
lista = tocheck.split()
junto = ''.join(lista)
inverso = ''
#inverso = junto[::-1]
for i in range(len(junto)-1, -1, -1):
    inverso += junto[i]
print('O contrário de {} é {}.'.format(tocheck,inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não é um palíndromo.')