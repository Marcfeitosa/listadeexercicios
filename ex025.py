print("""Exercício 025 
Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome""")

nome_completo = input("Digite seu nome completo: ").strip().title()
if 'Silva' in nome_completo == True:
    print('Tem Silva no nome')
else:
    print('Não tem Silva no nome')

