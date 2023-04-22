"""
Desafio 102

Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial. Também coloque na função os docstrings.
"""
def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta. Padão = False.
    :return: O valor do fatorial de um número num.
    """
    f = 1
    for i in range(num, 0, -1):
        f *= i
        if show:
            print(f'{i} x ' if i > 1 else f'{i} = ', end='')
    return f


# Programa principal
n = int(input('Digite um número para calcular seu fatorial: '))
mostrar = input('Deseja mostrar o processo de cálculo? [S/N] ').upper()[0]
if mostrar == 'S':
    mostrar = True
else:
    mostrar = False
print(fatorial(n, mostrar))
help(fatorial)
