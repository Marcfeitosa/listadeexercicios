"""Exercício 092

Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por
acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além
da idade, com quantos anos a pessoa vai se aposentar."""
import datetime

empregados = []
trabalhador = {}

while True:
    trabalhador['nome'] = str(input('Nome: '))
    data_de_nascimento = str(input('Data de nascimento: (mes/dia/ano)'))
    trabalhador['nascimento'] = datetime.datetime.strptime(data_de_nascimento, "%m/%d/%Y")
    trabalhador['idade'] = (datetime.datetime.today().year - trabalhador['nascimento'].year)
    trabalhador['ctps'] = str(input('Número da carteira de trabalho (0 não tem): '))
    if trabalhador['ctps'] != 0:
        ano_de_contrato = str(input('Quando a pessoa foi contratada: '))
        trabalhador['contratação'] = datetime.datetime.strptime(ano_de_contrato, "%m/%d/%Y")
        trabalhador['salario'] = float(input('Salário: '))
        ano_de_aposentaria = (trabalhador['nascimento']-trabalhador['contratação'])
        trabalhador['aposentadoria'] = (ano_de_aposentaria + datetime.timedelta(days=365*35))/365
        empregados.append(trabalhador.copy())
    for i in empregados:
        for c, a in i.items():
            print(f'{c} = {a}')
    continua = str(input('Quer continuar: '))
    if continua not in 'Nn':
        print('=#'*40)
    else:
        break

for i in empregados:
    for c, a in i.items():
        print(f'{c} = {a}')

"""Solução Gunabara"""

from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Número da carteira de trabalho (0 não tem): '))
if trabalhador['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) -datetime.now().year)
print('+-'*30)
for c, a in i.items():
    print(f'{c} = {a}')
