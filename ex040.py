"""DESAFIO 40

Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:

- Média abaixo de 5.0:
REPROVADO

- Média entre 5.0 e 6.9:
RECUPERAÇÃO

- Média 7.0 ou superior:
APROVADO"""

nota1 = float(input('Qual foi a primeira média: '))
nota2 = float(input('Qual foi a segunda média: '))

mediafinal = (nota1 + nota2)/2

if mediafinal < 5.0:
    print("REPROVADO")
elif mediafinal >= 5.0 and mediafinal <= 6.9:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")

"""if 7 > mediafinal <= 5:
    print("RECUPERAÇÃO")
elif mediafinal < 5:
    print("REPROVADO")
else:
    print("APROVADO")"""