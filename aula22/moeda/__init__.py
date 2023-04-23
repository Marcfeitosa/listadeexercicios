def aumentar(preco=0, taxa=0, formato=False):
    """
    -> Função que aumenta um preço em uma dada taxa.
    :param preco: O preço que se quer aumentar.
    :param taxa: Qual a taxa que você deseja aumentar.
    :param formato: Quer a saída formatada ou não?
    :return: O valor aumentado com ou sem formato.
    """
    res = preco + (preco * taxa/100)
    return res if not formato else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    """
    -> Função que diminui um preço em uma dada taxa.
    :param preco: O preço que se quer diminuir.
    :param taxa: Qual a taxa que você deseja diminuir.
    :param formato: Quer a saída formatada ou não?
    :return: O valor diminuído com ou sem formato.
    """
    res = preco - (preco * taxa/100)
    return res if not formato else moeda(res)


def dobro(preco=0, formato=False):
    """
    -> Função que calcula o dobro de um preço.
    :param preco: O preço que se quer calcular o dobro.
    :param formato: Quer a saída formatada ou não?
    :return: O dobro do preço com ou sem formato.
    """
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco=0, formato=False):
    """
    -> Função que calcula a metade de um preço.
    :param preco: O preço que se quer calcular a metade.
    :param formato: Quer a saída formatada ou não?
    :return: A metade do preço com ou sem formato.
    """
    res = preco / 2
    return res if not formato else moeda(res)


def moeda(preco=0, moeda='R$'):
    """
    -> Função que formata um preço com o formato de moeda.
    :param preco: O preço a ser formatado.
    :param moeda: Qual moeda você deseja exibir.
    :return: O valor formatado com o símbolo da moeda.
    """
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=10, taxar=5):
    """
    -> Função que resume as informações sobre um preço.
    :param preco: O preço a ser analisado.
    :param taxaa: A taxa de aumento.
    :param taxar: A taxa de redução.
    """
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado:\t{moeda(preco)}')
    print(f'Dobro do preço:\t\t{dobro(preco, True)}')
    print(f'Metade do preço:\t{metade(preco, True)}')
    print(f'{taxaa}% de aumento:\t\t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução:\t\t{diminuir(preco, taxar, True)}')
    print('-' * 30)
