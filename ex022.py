print("""DESAFIO DA AULA 09
Desafio 022
Criar um programa que leia o nome  completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas
- O nome com todas as letras minúsculas
- Quantas letras ao todo(sem considerar espaços)
- Quantas letras tem o primeiro nome""")

print('Desafio 022')
nome = str(input('Digite o seu nome completo: ')).strip()
print('Seu nome em maiúsculo: 'nome.upper())
print('Seu nome em minúsculo: 'nome.lower())
lista_nome = nome.split()
letras = '-'.join(lista_nome)
print('O seu nome tem {} letras.'.format(len(letras)-letras.count('-')))
print('O seu primeiro nome tem {} letras.'.format(len(lista_nome[0])))
