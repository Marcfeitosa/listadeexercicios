"""Desafio 057
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
peça a digitação novamente até ter um valor correto."""
mcount = 0
sexo = str(input('Qual é o seu sexo? [M/F]')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('O anta... qual é o seu probema? Só existe Masculino (M) e Feminino (F).')).upper().strip()[0]
print('OK... grandes coisa!!!!')