from datetime import date
print("""Desafio 32
Faça um programa que leia um ano qualquer e diga se ele é bissexto ou não""")
ano = int(input('Digite um ano qualquer, se quiser analisar o ano atual digite 0: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano \033[1;36m{}\033[m é bissexto.'.format(ano))
else:
    print('O ano não \033[1;34m{}\033[m é bissexto.'.format(ano))