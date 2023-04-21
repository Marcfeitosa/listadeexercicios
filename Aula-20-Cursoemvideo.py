def lin():
    print('-' * 30)


# Programa Principal
lin()
print(' CURSO EM VÍDEO  ')
lin()
print(' APRENDA PYTHON  ')
lin()
print(' MÁRCIO FEITOSA  ')
lin()

def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)
    return(msg)

mensagem('SISTEMA DE ALUNOS')

def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


#inputs do programa principal
titulo('  CURSO EM VÍDEO  ')
titulo(' APRENDA PYTHON  ')
titulo(' MÁRCIO FEITOSA  ')


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f' A soma de A + B = {s}')

#Programa Principal
soma(4, 5)

def contador(*num):
    print(num)

contador(2, 1, 7, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

def contador2(*num):
    for valor in num:
        print(valor, end='')
    print(' FIM!')

contador2(2, 1, 7)
contador2(8, 0)
contador2(4, 4, 7, 6, 2)

def contador2(*num):
    tam = len(num)
    print(f'Recebi os valores {num}  e são ao todo {tam} números')

contador2(2, 1, 7)
contador2(8, 0)
contador2(4, 4, 7, 6, 2)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores=[7, 2, 5, 0, 4]
dobra(valores)
print(valores)

def soma(* valores):
    s = 0
    for num in valores:
        s += num
        print(f"somando os valores {valores} temos {s}")

soma(5, 2)
soma(2, 9, 4)
