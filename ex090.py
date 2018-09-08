"""Exercício 090

Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela."""

aluno = {}
turma = []
x = int(input('Quantos alunos exitem na turma: '))

for alunos in range(0, x):
    aluno['nome'] = str(input('Nome do aluno: '))
    aluno['media'] = float(input(f'Média do aluno {aluno["nome"]}: '))
    if aluno['media'] >= 7:
        aluno['situação'] = str('Aprovado')
    else:
        aluno['situação'] = str('Reprovado')
    turma.append(aluno.copy())

for estudande in turma:
    for cabeçalho, atributos in estudande.items():
        print(f'{cabeçalho} = {atributos}')
    print('-='*30)

