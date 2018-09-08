"""Desafio 077

Crie um programa que tenha uma tupla com várias palavras (nâo usar acentos).

Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""

import selenium

tupla = ('cadeira', 'vaso', 'mesa', 'sofa', 'livro', 'TV', 'puff', 'chuveiro', 'tapete')
for palavra in tupla:
    print(f'\nA palavra {palavra.upper()} tem as vogais ', end="")
    vogais = ('a', 'e', 'i', 'o', 'u')
    for letra in palavra:
        if letra.lower() in vogais:
            print(letra, end=" ")

tupla = ('cadeira', 'vaso', 'mesa', 'sofa', 'livro', 'TV', 'puff', 'chuveiro', 'tapete')
for palavra in tupla:
    print(f'\nA palavra {palavra.upper()} tem as vogais ', end="")
    for letra in palavra:
        if letra.lower() in 'aeiouáéíóúàãõâêô':
            print(letra, end=" ")
