"""DESAFIO 41

A confederação nacional de natação precisa de um programa que leia o ano de
nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: Sênior
- Acima: MASTER"""

idadeatleta = int(input("Qual é a idade do atleta? "))

if idadeatleta <= 9:
    print("MIRIM")
elif idadeatleta > 9 and idadeatleta <= 14:
    print("INFANTIL")
elif idadeatleta > 14 and idadeatleta <= 19:
    print("JUNIOR")
elif idadeatleta >19 and idadeatleta <= 25:
    print("SÊNIOR")
else:
    print("MASTER")

if idadeatleta <= 9:
    print("MIRIM")
elif idadeatleta <= 14:
    print("INFANTIL")
elif idadeatleta <= 19:
    print("JUNIOR")
elif idadeatleta <= 25:
    print("SÊNIOR")
else:
    print("MASTER")