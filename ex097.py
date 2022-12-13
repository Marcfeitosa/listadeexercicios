cores = {'limpa': '\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'roxo':'\033[35m',
         'azulclaro':'\033[36m',
         'cinza':'\033[37m'}

print("""Desafio 097
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro
e mostre uma mensagem com tamanho adaptável

Ex: escreva('Olá, Mundo!')

Saída:
~~~~~~~~~~~~~~~~~~
    Olá, Mundo!
~~~~~~~~~~~~~~~~~~

""")

def escreva(msg):
    x = len(msg)
    print(("~" * x) + "~" * 8)
    print(f'    {msg}    ')
    print(("~" * x) + "~" * 8)


#variáveis
escreva(input("Digite qualquer coisa e veja as margens se adaptarem: "))

def escreva(msg):
    tam = len(msg) + 4
    print("~" * tam)
    print(f'  {msg}')
    print("~" * tam)

escreva(input("Digite qualquer coisa e veja as margens se adaptarem: "))
escreva(input("Digite outra coisa: "))
escreva(input("Mais uma vez: "))

