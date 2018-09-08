"""Exercício 094

Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos
os dicionários em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas

B) A média de idade do grupo.

C) Uma lista com todas as mulheres.

D) Uma lista com todas as pessoas com idade acima da média."""

import statistics

pessoa = {}
conjunto = []

while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: '))
    pessoa['idade'] = str(input('idade: '))
    conjunto.append(pessoa.copy())
    continua = str(input('Gostaria de continuar? '))
    if continua not in 'Nn':
        print('=+'*40)
    else:
        break
print(f'Foram cadastradas {len(conjunto)} pessoas')
print()


soma_idade = []
for percorre_pessoa in conjunto:
    for acha_idade, coloca_idade_na_lista in percorre_pessoa.items():
        if acha_idade == 'idade':
            soma_idade.append(coloca_idade_na_lista)
soma_idade = list(map(int, soma_idade))
print(f'A média de idade é de {statistics.mean(soma_idade)}')
print()

mulheres = []
for percorre_pessoa in conjunto:
    for acha_sexo, coloca_na_lista in percorre_pessoa.items():
        if acha_sexo == 'sexo':
            mulheres.append(coloca_na_lista)
print()
print(f'existem {mulheres.count("f")} mulheres')
print()
print('=+'*40)
idade_acima_media = []
media = statistics.mean(soma_idade)
for percorre_pessoa in conjunto:
    for idade, acima_media in percorre_pessoa.items():
        if idade == 'idade' and int(acima_media) > int(media):
            idade_acima_media.append(percorre_pessoa["nome"])
print()
print(f'Estas são as pessoas acima da média de idade {idade_acima_media}')