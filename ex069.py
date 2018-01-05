"""Desafio 069

Crie um program que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada o programa deverá perguntar se o
usuário quer ou não continuar. No final mostre:

A) quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos."""

contm = contf = cont18 = cont20 = idade = 0
continuar = 'S'
while True:
    sexo = str(input('Qual é o sexo da pessoa: [M/F] ')).upper().strip()[0]
    if sexo == 'M':
        contm += 1
    elif sexo == 'F':
        contf += 1
    else:
        while sexo != 'M' or sexo != 'F':
            sexo = str(input('Entrada inválida, tente novamente.')).upper().strip()[0]
    idade = 0
    while False:
        print('nenhum número foi digitado, tente novamente. ')
    idade = int(input('Qual é a idade dessa pessoa? '))
    if idade > 18:
        cont18 += 1
    elif idade < 20 and sexo == 'M':
        cont20 += 1
    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    print('~'*20)
    while continuar not in 'SN':
        continuar = str(input('Entrada inválida, tente novamente. '))
    if continuar == 'N':
        break
print('~'*20)
print(f'Há {cont18} pessoas com mais de 18 anos nesta lista.')
print(f'Há {contm} homens nessa lista.')
print(f'Há {cont20} mulheres com menos de 20 anos.')
