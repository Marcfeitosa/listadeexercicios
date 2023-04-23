"""
Desafio 112

Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários.

A função também tem que aceitar o usuário inputando os números com casas decimais separados por ',' ao invés de '.'.

"""

from utilidadesCeV import moeda, dados

p = dados.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 20, 12)
