print("""Exercício 027
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.""")

nome = input('Digite o seu nome completo: ').strip()
nomediv = nome.split()
print('O primeiro nome é: {}'.format(nomediv[0]))
print('O último nome é: {}'.format(nomediv[-1]))