"""Exercício 51

Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética.
No final, mostre os 10 primeiros termos dessa progressão"""

print('='*25)
print('Progressão aritmética')
print('='*25)
progress = int(input('Digite a razão da progressão aritmética: '))
primeirotermo = int(input('Digite o primeiro termo da progressão aritmética: '))
ultimotermo = int(input('qual é o último termo que você quer? '))
ultimotermocalc = primeirotermo+((ultimotermo)*progress)
for i in range(primeirotermo,ultimotermocalc,progress):
    print('{} '.format(i), end='-> ')
print('ACABOU')