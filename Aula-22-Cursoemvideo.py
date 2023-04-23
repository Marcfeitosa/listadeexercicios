import aula22.uteis as uteis

num = int(input('Digite um valor'))
fat = uteis.fatorial(num)
print(f'O fatorial de{num} é {fat}')
print(f'O dobro de {num} é {uteis.dobro(num)}')
print(f'O triplo de {num} é {uteis.triplo(num)}')


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

"""
Desafio 108

Adapte o código do desafio 107, criando uma funão adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.

O programa vai usar o módulo assim:

from aula22 import moeda
p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.dimiuir(p, 13)}')

"""

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

"""
Desafio 110

Adicione ao módulo moeda.py, criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funões que já temos no mpodulo criado até aqui.

o programa vai funcionar assim:
p = float(input('Digite o preço: R$'))
moeda.resumo(p, 80, 35)

"""

"""
Desafio 111

Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dados.
Transfira todas as funções utilizadas nos desafios 107, 108, 109 para o primeiro pacote e mantenha tudo funcionando.

"""
"""
Desafio 112

Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários.

A funçao também tem que aceitar o usuário inputando os números com casas decimais separados por ',' ao invés de '.'.

"""