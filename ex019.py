print('Eercício 019')
from random import randint, choice

elementolist = randint(0, 3)
listalunos = ["Vivian","Arthur","Eu","Gucci"]
print('Escolher o aluno que vai apagar o quadro. O Python escolheu o aluno {}'.format(listalunos[elementolist]))
print('com a método choice o Python escolheu: {}'.format(choice(listalunos)))