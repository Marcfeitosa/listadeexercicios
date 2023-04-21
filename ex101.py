"""
Desafio 101:

Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal, indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
"""

from datetime import date

def voto(data_nascimento):
    idade = date.today() - data_nascimento
    anos = idade.days // 365
    meses = (idade.days % 365) // 30
    dias = (idade.days % 365) % 30

    if anos < 16:
        return f'Com {anos} anos, voto NEGADO.'
    elif 18 <= anos < 70:
        return f'Com {anos} anos, voto OBRIGATÓRIO.'
    else:
        return f'Com {anos} anos, voto OPCIONAL.'
        
data_str = input('Digite a data de nascimento no formato DD/MM/AAAA: ')
dia, mes, ano = map(int, data_str.split('/'))
data_nascimento = date(ano, mes, dia)
print(voto(data_nascimento))

