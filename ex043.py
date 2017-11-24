"""ESAFIO 043

Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcula seu IMC e mostre o seu status, de acordo
com a tabela abaixo:

- Abaixo de 18.5: Abaixo de Peso

- Entre 18.5 e 25: Peso ideal

- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: obesidade mórbida"""

peso = float(input("Qual é o seu peso? "))
altura = float(input("Qual é a sa altura? "))
imc = peso/(altura**2)'Sinal do quadrado'

if imc <= 18.5:
    print("Abaixo do Peso")
elif imc > 18.5 and imc <= 25:
    print("Peso ideal")
elif imc > 25 and imc <= 30:
    print("Sobrepeso")
elif imc > 30 and imc <= 40:
    print("Obesidade")
else:
    print("Obesidade Mórbida")