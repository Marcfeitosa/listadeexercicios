x=float(input('vamos converter os metros, digite a medida em metros a ser convertida: '))
km=x/1000
hm=x/100
dam=x/10
dm=x*10
cm=x*100
mm=x*1000
print('As medidas são conforme a seguir: \nQuilômetros: {} \nHectômetros: {} \nDecâmetros: {} \nDecímetros: {} \nCentímetros: {} \nMilímetros: {}'.format(km,hm,dam,dm,cm,mm))
