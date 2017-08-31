print("""Desafio 34
Faça um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.200,00 calcule um aumento de 10%.
Para salários inferiores ou iguais, o aumento é de 15%""")
sal = float(input('Qual é o seu salário? '))
if sal > 1200.00:
    print('Parabéns, ganhou um aumento de 15%, o seu novo salário é de {}{}{}.'.format('\033[31m', sal*1.15, '\033[m'))
else:
    print('Parabéns, ganhou um aumento de 10%, o seu novo salário é de {}.'.format('\033[7;30m', sal*1.10, '\033[m'))