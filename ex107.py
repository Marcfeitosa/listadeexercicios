"""
Desafio 107

Crie um módulo chamado moeda.py que tenha as funções incorporadas: aumentar(), diminuir(), dobro() e metade().py

Faça também um programa que importe esse módulo e use algumas dessas funções.py

O programa vai usar o módulo assim:

from aula22 import moeda
p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.dimiuir(p, 13)}')

"""

from aula22.moeda import aumentar, diminuir, dobro, metade

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {metade(p)}')
print(f'O dobro de {p} é {dobro(p)}')
print(f'Aumentando 10%, temos {aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {diminuir(p, 13)}')
