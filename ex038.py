"""DESAFIO 38

Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais"""

num1 = float(input('Digite o primeiro número que desejas comparar: '))
num2 = float(input('Digite o segundo número que desejas comparar: '))

if num1 > num2:
    print('O primeiro valor é maior')
elif num1 < num2:
    print('O segundo O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')