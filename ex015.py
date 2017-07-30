t=int(input('Quantos dias alugados? '))
km=float(input('Quantos Km rodados? '))
v1=t*60
v2=km*0.15
vf=v1+v2
print('O valor a ser pago é de {:.2f}'.format(vf))