"""DESAFIO 61

Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da
progressão usando a estrutura while"""

print('='*25)
print('Progressão aritmética 3')
print('='*25)
primeirotermo = int(input('Digite o primeiro termo da progressão aritmética: '))
progress = int(input('Digite a razão da progressão aritmética: '))
ultimotermocalc = primeirotermo+((10-1)*progress)
print(primeirotermo,end='; ')
termoacrescimo = primeirotermo
while ultimotermocalc > termoacrescimo:
    termoacrescimo += progress
    print(termoacrescimo,end='; ')
print('')
print('='*25)
print('')
print('FIM DA PROGRESSÃO ARITMÉTICA')