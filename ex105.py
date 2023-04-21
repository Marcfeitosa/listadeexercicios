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

def notas(*args, situacao=False):
    """
    -> Função para analisar notas e situação de alunos.
    :param args: uma ou mais notas dos alunos (aceita várias)
    :param situacao: (opcional) indica se deve ou não mostrar a situação do aluno.
    :return: dicionário com informações sobre as notas da turma.
    """
    notas_dict = {'Quantidade de notas': len(args),
                  'Maior nota': max(args),
                  'Menor nota': min(args),
                  'Média da turma': sum(args) / len(args)}

    if situacao:
        if notas_dict['Média da turma'] >= 7:
            notas_dict['Situação'] = 'APROVADO'
        elif notas_dict['Média da turma'] < 5:
            notas_dict['Situação'] = 'REPROVADO'
        else:
            notas_dict['Situação'] = 'RECUPERAÇÃO'

    return notas_dict


# Input de notas
notas_aluno = []
while True:
    nota = input("Digite uma nota (ou 'q' para sair): ")
    if nota == 'q':
        break
    notas_aluno.append(float(nota))

# Chamada da função e impressão do resultado
info_notas = notas(*notas_aluno, situacao=True)
print(info_notas)
