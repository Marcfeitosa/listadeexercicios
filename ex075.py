"""Desafio 075

Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares."""

n1 = int(input('vamos pedir quatro números, digite o primeiro:'))
n2 = int(input('Digite o segundo nº:'))
n3 = int(input('Digite o terceiro nº:'))
n4 = int(input('Digite o quarto nº:'))

verificans = (n1, n2, n3, n4)
print(f'O número 9 aparece {verificans.count(9)} vezes.')
if 9 not in verificans:
    print(f'O valor 9 não foi digitado.')
else:
    print(f'primeiro valor 3 foi digitado na {verificans.index(3)+1}ª vez que pedimos, para digitar.')
i = 0
for i in verificans:
    x = i % 2
    if x == 0:
        print('par')
    else:
        print('impar')
    i += 1

print('-='*20)

numeros = (int(input('Digite um número: ')),int(input('Digite outro número: ')),int(input('Digite mais um número: ')),
           int(input('Digite um número mais uma vez: ')))

print(f'Voce digitou os valores {numeros}')
print(f'O número 9 aparece {numeros.count(9)} vezes.')
print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posiçao.')
for i in numeros:
    x = i % 2
    if x == 0:
        print('par')
    else:
        print('impar')
    i += 1