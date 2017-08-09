print("""Exercício 026
Fazer um programa que leia uma frase pelo teclado e mostre:
    - Quantas vezes aparece a letra 'a'.
    - Em que posição ela aparece a primeira vez.
    - Em que posição ela aparece a última vez.""")

frase = input('Digite uma frase: ').strip()
frasemin = frase.lower()
contagem = frasemin.count('a')
if contagem < 1:
    print("Não tem 'a' na frase")
elif contagem == 1:
    print("A letra 'a' aparece {} vez.".format(contagem))
else:
    print("A letra 'a' aparece {} vezes.".format(contagem))
print("A letra 'a' aparece pela primeira vez na posição {}.".format(frasemin.find('a')+1))
print("A letra 'a' aparece pela primeira vez na posição {}.".format(frasemin.rfind('a')+1))
