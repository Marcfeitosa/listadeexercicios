"""Exercício 79
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro,
ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente."""

continuar = 'S'
listanumerica = []
while continuar == 'S':
    entrada = int(input(f'Digite um valor '))
    if entrada in listanumerica:
        print('Valor duplicado! Não vou adicionar...')
    else:
        listanumerica.append(entrada)
        print('Valor adicionado com sucesso.')
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
listanumerica.sort()
print(f'você adicionou os valores {listanumerica}')

print()
print('-='*30)
print()

numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N}'))
    if r in 'Nn':
        break
numeros.sort()
print(f'Você adicionou os valores {numeros}')
