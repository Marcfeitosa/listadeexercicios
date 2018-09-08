"""Desafio 076

Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência.

No final, mostre uma listagem de preços, organizando os dados em forma tabular."""

#for i in range(1, 10, 1):
#    print('produto', i, " | preço: '")

produto1 = 4.50
produto2 = 5.50
produto3 = 3.00
produto4 = 2.85
produto5 = 1.90
produto6 = 3.67
produto7 = 2.95
produto8 = 7.50
produto9 = 9.05
produto10 = 8.00

produtoseprecos = ('4.50', '5.50', '3.00', '2.85', '1.90', '3.67', '2.95', '7.50', '9.05', '8.00')

#for pos in range(0, 10, 1):
#    print(f'produto {pos+1} | preço: {produtoseprecos[pos]}')

print('-='*20)
print('-='*20)

produtoseprecos2 = (('produto1', 4.50), ('produto2', 5.50), ('produto3', 3.00), ('produto4', 2.85), ('produto5', 1.90),
                    ('produto6', 3.67), ('produto7', 2.95), ('produto8', 7.50), ('produto9', 9.05), ('produto10', 8.00))

for pos1 in(produtoseprecos2):
    print(f'{pos1[0]} | preço: R$ {pos1[1]}')

produtoseprecos3 = ('produto1', 4.50, 'produto2', 5.50, 'produto3', 3.00, 'produto4', 2.85, 'produto5', 1.90,
                    'produto6', 3.67, 'produto7', 2.95, 'produto8', 7.50, 'produto9', 9.05, 'produto10', 8.00)

print('-'*40)
print('Listagem de preços')
print('-'*40)
for pos in range(0, len(produtoseprecos3)):
    if pos % 2 == 0:
        print(f'{produtoseprecos3[pos]:.<30}', end='')
    else:
        print(f'R$ {produtoseprecos3[pos]:>2}')
print('-'*40)
