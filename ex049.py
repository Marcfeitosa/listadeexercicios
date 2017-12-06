"""Exercício 49

Refaça o desafio 9, mostrando a tabuada de um número que o usuário escolher. Só que agora utilizando um laço FOR"""

x = int(input('Digite um número para vermos a sua tabuada: '))
for i in range(0,11,1):
    print('{} x {} = {}'.format(x,i,x*i))