print("""Desafio 023
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
ex: Digite um número: 1834

unidade: 4
dezena:3
centena:8
milhar:1""")



while True:
    x = input( 'Digite um número de 0 a 9999: ' )
    if len(x) > 0 and len(x) <= 4:
        break
    print('Errroooooou')

# 1346
#milhar = x / 1000 # 1
#x -= 1000 * milhar  #346
#centena = x / 100 # 3
#x -= 100 * centena # 46
#dezena = x / 10 # 4
#x -= 10 * dezena # 6
#unidade = x #6

unidades = ['unidade', 'dezena', 'centena', 'milhar']

for i in range(len(x), 0, -1):
    print('{} = {}'.format(unidades[len(x)-i], int( x[i-1] ) ) )


    #x = input('Digite um número de 0 a 9999: ')
    #y = int(x)
#print('unidade = {}'.format(int(x[3])))
#print('dezena = {}'.format(int(x[2])))
#print('centena = {}'.format(int(x[1])))
#print('milhar = {}'.format(int(x[0])))