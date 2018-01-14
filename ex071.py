"""Desafio 071

Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

Obs. Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1"""

print("""Cédulas disponíveis:
            R$ 50   R$ 20
            R$ 10   R$ 1""")

notas50 = notas20 = notas10 = notas1 = 0
valorsacado = int(input('Qual é o valor a ser sacado: '))
while valorsacado <= 0:
    valorsacado = int(input('Qual é o valor a ser sacado: '))
if valorsacado >= 50:
    notas50 = int(valorsacado/50)
    resto = valorsacado % 50
    if resto > 0:
        notas20 = int(resto / 20)
        resto = resto % 20
        if resto > 0:
            notas10 = int(resto / 10)
            resto = resto % 10
            if resto > 0:
                notas1 = int(resto / 1)
elif valorsacado < 50 and valorsacado >= 20:
    notas20 = int(valorsacado/20)
    resto = notas20 % 20
    if resto > 0:
        notas10 = int(resto / 10)
        resto = resto % 10
        if resto > 0:
            notas1 = int(resto / 1)
elif valorsacado < 20 and valorsacado >= 10:
    notas10 = int(valorsacado/10)
    resto = notas10 % 10
    if resto > 0:
        notas1 = int(resto / 1)
else:
    notas1 = int(valorsacado/1)
if notas50 > 0:
    print(f'Serão sacadas {notas50} cédulas de R$ 50.')
if notas20 > 0:
    print(f'Serão sacadas {notas20} cédulas de R$ 20.')
if notas10 > 0:
    print(f'Serão sacadas {notas10} cédulas de R$ 10.')
if notas1 > 0:
    print(f'Serão sacadas {notas1} cédulas de R$ 1.')
print('~'*40)
print(f'FIM DA OPERAÇÃO')
