"""Desafio 39

Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:

- Se ele ainda vai se alistar ao serviço militar (e quanto tempo falta)
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento (quanto tempo passou)

O programa deve mostrar o tempo que falta e tempo que excedeu do alistamento"""

sexo = str(input("""Você é homem ou mulher?
                    H - para Homem
                    ou 
                    M - para Mulher """))
if sexo.upper() == 'M':
    print('Você não precisa se alistar')
elif sexo.upper() == 'H':
    idade = int(input('Qual é a sua idade? '))

    def definição_anos():
        if tempoalistamento == 1:
            return 'ano'
        else:
            return  'anos'

    if idade == 18:
        print('É tempo de se alistar')
    elif idade < 18:
        tempoalistamento = 18 - idade
        print('Ainda faltam {} {} para o seu alistamento'.format(tempoalistamento,definição_anos()))
    else:
        print('Você já deveria ter se alistado')

    from datetime import date
    atual = date.today().year
    nascimento = int(input('Ano de nascmiento: '))
    anosparasealistar = atual - nascimento

    def definição_anos2():
        if anosparasealistar == 1:
            return 'ano'
        else:
            return  'anos'

    if atual - nascimento == 18:
        print('Se alista que está na hora...')
    elif atual - nascimento <= 17:
        print('calma, ainda faltam {} {} para o seu alistamento.'.format(anosparasealistar,definição_anos2()))
        print('Seu alistamento será em {}.'.format(nascimento + 18))
    else:
        anosparasealistar2 = atual - (nascimento + 18)
        print('Corre para se alistar, você já está {} {} atrasado.'.format(anosparasealistar2,definição_anos2()))
        print("Seu alistamento foi em {}.".format(nascimento+18))
else:
    print('Não existe outro sexo ou outra indicação de sexo diferente de H ou M')