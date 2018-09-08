"""Desafio 84
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""

pessoas = []
person = []
while True:
    person.append(str(input('Qual é o nome da pessoa? ')))
    person.append(float(input("Qual é o peso dessa pessoa? ")))
    pessoas.append(person[:])
    continua = str(input('Quer continuar? [S/N}'))
    if continua not in "Nn":
        person.clear()
    else:
        break
print()
print('=*'*30)
print()
print(f'Os dados cadastrados foram: {pessoas}')
print(f'foram cadastradas {len(pessoas)} pessoas')
maxmin = []
for i in pessoas:
    maxmin.append(i[1])
print(f'O maior peso digitado foi {max(maxmin)}. Peso de ', end='')
pessoamaispesada = max(maxmin)
for i in pessoas:
    if pessoamaispesada == i[1]:
        print(f'{i[0]}')
print(f'O menor peso digitado foi {min(maxmin)}. peso de ', end='')
pessoamaisleve = min(maxmin)
for i in pessoas:
    if pessoamaisleve == i[1]:
        print(f'{i[0]}')

"""Solução do Guanabara"""
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append((float(input('Peso: '))))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print()
print('=+'*30)
print()
print(f'Os dados foram {princ}')
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}Kg.', end='')
for p in princ:
    if p[1] == mai:
        print(f'peso de [{p[0]}]')
print(f'O menor peso foi de [{men}Kg]', end='')
for p in princ:
    if p[1] == men:
        print(f'peso de {p[0]}')
