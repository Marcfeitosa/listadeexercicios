"""
Desafio 109

Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda, desenvolvida no Desafio 108

O programa vai usar essa modificação assim:

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.dimiuir(p, 13, True)}')
"""

from aula22.moeda import aumentar, diminuir, dobro, metade, moeda

preco = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda(preco)} é {metade(preco, True)}.')
print(f'O dobro de {moeda(preco)} é {dobro(preco, True)}.')
print(f'Aumentando 10%, temos {aumentar(preco, 10, True)}.')
print(f'Reduzindo 13%, temos {diminuir(preco, 13, True)}.')
