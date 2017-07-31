print('exercício 017')
from math import sqrt, hypot

catetooposto = float(input('qual é o comprimento do cateto oposto: '))
catetoadjacente = float(input('qual é o comprimento do cateto adjacente: '))
hipotenusa = hypot(catetooposto, catetoadjacente)
print("a hipotenusa é igual à {}.".format(sqrt((catetooposto ** 2) + (catetoadjacente ** 2))))
print('tirando a prova dos nova com a Hipotenusa: {}'.format(hipotenusa))