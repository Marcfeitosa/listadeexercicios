l=float(input('Largura da parede: '))
h=float(input('Altura da parede: '))
print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m.'.format(l,h,(l*h)))
print('Para pintar essa parede, você precisará de {:.2f} litros de tinta.'.format((l*h)/2))
