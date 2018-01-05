print("""DESAFIO 62

Melhore o desafio 61, pergunte para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando
ele disser que quer mostrar 0 termos.""")

print('='*25)
print('Progressão aritmética 3')
print('='*25)
primeiro = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))
while razao < 0:
    print('Não existe progressão 0, tente novamente, eu sei que você consegue.')
termo = primeiro
contador = 1
total = 0
continua = 10
while continua != 0:
    total += continua
    while contador <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        contador += 1
    print('PAUSA')
    continua = int(input('Quantos termos você quer mostrar a mais? '))
print('')
print('Progressão finalizada com {} termos mostrados.'.format(total))
print('')
print('=' * 25)
print('')
print('FIM DA PROGRESSÃO ARITMÉTICA')