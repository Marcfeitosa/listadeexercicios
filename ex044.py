"""DESAFIO 044

Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

- À VSITA: dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""

produto = str(input("Qual é o produto? "))
preço = float(input("Qual é o preço de {}? ".format(produto)))
listapagamento = ["Dinheiro","Cheque","Cartão","2x Cartão","3x Cartão"]
formadepagamento = int(input("""Qual é a forma de pagamento escolhida? 
                                    1- Dinheiro:
                                    2- Cheque:
                                    3- Cartão:
                                    4- 2x Cartão:
                                    5- 3x Cartão: """))
if formadepagamento == 1:
    print('\033[1;34mVocê terá 10% de desconto, você pagará {}.\033[m'.format(preço*0.9))
elif formadepagamento == 2:
    print("Você terá 10% de desconto, você pagará {}.".format(preço*0.9))
elif formadepagamento == 3:
    print("Você terá 5% de desconto, você pagará {}.".format(preço*0.95))
elif formadepagamento == 4:
    print("Você não tem desconto, preço final de {}, as parcelas serão de {}.".format(preço, preço/2))
else:
    numparcelas = int(input('Em quantas parcelas? '))
    print("VOcê terá um acréxscimo de 20% de juros. O preço final é de {}, cada parcela será de {}.".format(preço*1.20, (preço*1.2)/numparcelas))