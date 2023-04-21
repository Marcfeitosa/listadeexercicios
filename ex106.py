"""
Desafio 106

Faça um mini-sistema que utilize o Interactive help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrerará.

OBS: use cores. Cada bloco de mensagem deve vir numa cor diferente. 

"""

from time import sleep

def ajuda(comando):
    titulo(f"Acessando o manual do comando '{comando}'", cor='azul')
    print(cores['branco'])
    help(comando)
    print(cores['limpa'])


def titulo(msg, cor='limpa'):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(cores['limpa'], end='')
    sleep(1)


cores = {
    'limpa': '\033[m',
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'amarelo': '\033[1;33m',
    'azul': '\033[1;34m',
    'roxo': '\033[1;35m',
    'ciano': '\033[1;36m',
    'branco': '\033[30m'
}

while True:
    titulo('SISTEMA DE AJUDA PyHELP', cor='verde')
    comando = input('Função ou Biblioteca > ').strip().lower()
    if comando == 'fim':
        break
    ajuda(comando)
titulo('Até logo!', cor='amarelo')
