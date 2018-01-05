"""Desafio 067

Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitados for negativo."""

contador = numero = 0
while numero >= 0:
    numero = int(input("Digite um número para verificarmos a tabuada: "))
    if numero > 0:
        for i in range(1, 11):
            contador += 1
            print(f'{contador} x {numero} =  {contador*numero}')
        contador = 0
    else:
        print('Programa de tabuada terminado, você digitou um número negativo... Eu não gosto de números negativos')
