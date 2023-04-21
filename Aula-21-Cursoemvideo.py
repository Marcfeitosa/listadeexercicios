# Docstrings

def contador(i,f,p):
    """
    -> Faz uma contagem e mostra na tela.
    :parâmetro i: início da contagem
    :parâmetro f: fim da contagem
    :parâmetro p: passo da contagem
    :return: sem retorno
    função criada por Márcio Feitosa
    """
    c=i
    while c <= f:
        print(f'{c}',end='..')
        c += p
    print('FIM!')

contador(2,10,2)

help(contador)

# Parâmetros Opcionais
def somar(a=0,b=0,c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    Função criada por Márcio
    """
    s=a+b+c
    print(f'A soma de tudo é {s}')

#somar(3,2,5)

somar(b=4, a=2)

# Escopo de variáveis

def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

# Programa principal da def teste()
n = 2
print(f'No programa principal, n vale {n}')
x = teste()
print(f'No programa principal, x vale {x}')

def somar2(a=0,b=0,c=0):
    s = a+b+c
    return s

r1 = somar2(3,2,5)
r2 = somar2(2,2)
r3 = somar2(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')

#Exercício de sala

def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

# Exercício de sala 2
def par(n=0):
    if n % 2 == 0:
        return True

num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')


"""
Desafio 101:

Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal, indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

"""

"""
Desafio 102

Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial. Também coloque na função os docstrings.

"""

"""
Desafio 103:

 Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
 O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha seido informado corretamente.

"""

"""
Desafio 104:

Crie um programa que tenha uma função LeiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico

ex:
n=LeiaInt('Digite um n')

"""

"""
Desafio 105

Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings da função

"""

"""
Desafio 106

Faça um mini-sistema que utilize o Interactive help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrerará.

OBS: use cores. Cada bloco de mensagem deve vir numa cor diferente. 

"""