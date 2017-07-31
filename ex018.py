print('Exercício 018')
from math import radians, sin, cos, tan

an = float(input('Digite um ângulo: '))
sen = sin(radians(an))
coss = cos(radians(an))
tang = tan(radians(an))
print("O seno do ângulo {:.2f} é {:.2f}, o coseno é {:.2f} e a tangente é {:.2f}".format(an,sen,coss,tang))