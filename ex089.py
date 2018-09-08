"""Desafio 89
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada
aluno individualmente."""

import numpy

turma = []
aluno = []

while True:
    aluno.append(str(input('Qual é o nome do Aluno: ')))
    aluno.append(float(input('Qual é a primeira nota do Aluno: ')))
    aluno.append(float(input('Qual é a segunda nota do Aluno: ')))
    aluno.append(float((aluno[1]+aluno[2])/2))
    turma.append(aluno[:])
    aluno.clear()
    continua = str(input('Quer continuar? [S/N}'))
    if continua not in 'Nn':
        aluno.clear()
    else:
        break

print()
print('=#'*30)
print()

print(numpy.matrix(turma))

print()
print('=#'*30)
print()

busca = str(input('De qual aluno você quer saber as notas? '))
for i in turma:
    while busca not in turma:
        busca = str(input('Nome de aluno não encontrado, favor digitar novamente: '))
    if i[0] == busca:
        print(i)

