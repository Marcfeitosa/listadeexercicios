"""Exercício 80
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção
(sem usar o sort()). No final, mostre a lista ordenada na tela.
"""

listaemordem = []
for i in range(0, 5):
    valor = int(input(f'Digite o {i+1}° valor: '))
    if valor > valor:
        for i in listaemordem:
            listaemordem.insert(i+1, valor)
        else:
            listaemordem.insert(i - 1, valor)
print(listaemordem)

listaemordem2 = []
for c in range(0, 5):
    n = int(input(f'Digite o {i+1}° valor: '))
    if n == 0 or n > listaemordem2[-1]:
        listaemordem2.append(c)
    else:
        pos = 0
        while pos < len(listaemordem2):
            if n <= listaemordem2[pos]:
                listaemordem2.insert(pos, n)
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {listaemordem2}')

