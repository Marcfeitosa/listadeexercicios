"""Desafio 073

Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:

A) Apenas os 5 primeiros colocados.

B)Os últimos 4 colocados da tabela.

C)Uma lista com os times dem ordem alfabética.

D)Em que posição na tabela está o time da Chapecoense."""

campeonatobrasileiro = ('Atlético - MG','Flamengo - RJ','Corinthians - SP','Palmeiras - SP','Fluminense - RJ','América - MG',
                        'São Paulo - SP','Grêmio - RS','Vasco da Gama - RJ','Internacional - RS','Botafogo - RJ','Sport - PE',
                        'Cruzeiro - MG','Vitória - BA','Santos - SP','Chapecoense - SC','Atlético - PR','Bahia - BA',
                        'Ceará - CE','Paraná - PR')

print(campeonatobrasileiro)
print('-='*20)
print(campeonatobrasileiro[0:5])
print('-='*20)
print(campeonatobrasileiro[-19:16])
print('-='*20)
print(sorted(campeonatobrasileiro))
print('-='*20)
for pos, time in enumerate(campeonatobrasileiro):
    if time == 'Chapecoense - SC':
        print(f'A {time} está na {pos+1}ª posição')
print('-='*20)
print(f'A Chapecpecoense está na {campeonatobrasileiro.index("Chapecoense - SC")+1}ª posição')
