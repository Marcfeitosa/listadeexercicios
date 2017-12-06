"""Exercício 56

Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo:
- Qual é o nome do homem mais velho:
- Quantas mulheres têm menos de 20 anos:"""

for i in range(0,4):
    nome = str(input('Qual é o seu nome? '))
    idade = int(input('Qual é a sua idade? '))
    sexo = str(input('Masculino ou Feminino? (M para Masculino / F para Feminino: ')).strip().upper()
    lista = [i]
    lista