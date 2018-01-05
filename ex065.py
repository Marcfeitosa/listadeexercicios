print("""DESAFIO 065

Crie um programa que leia varios números inteiros no teclado. No final da execução, mostre a média
entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário
se ele quer ou não continuar a digitar valores.""")

n = cont = soma = maior = menor = 0
mais = 'S'
while mais == 'S':
    n = int(input('Digite um número inteiro: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    mais = str(input('Quer continuar? [S/N]')).upper().strip()[0]
print('A soma de todos os números digitados é de {}, a média dos valores é {}, foram digitados {} números.'.format(soma, soma/cont, cont))
print('O menor valor foi {} e o maior foi {}.'.format(menor, maior))
