def aumentar(valor=0, taxa=0, formato=False):
    '''

    :param valor: Parametro que informa o valor solicitado ou preço do produto
    :param taxa: taxa de aumento de porcentagem(Aumentar e diminuir)
    :param formato: Parametro de formatação de moeda
    :return: Retorna o valor solicitado e formata caso seja True
    '''
    a = valor + (valor*taxa/100)
    return a if formato is False else moeda(a)


def diminuir(valor=0, taxa=0, formato=False):
    d = valor - (valor*taxa/100)
    return d if formato is False else moeda(d)


def dobro(valor=0, formato=False):
    db = valor * 2
    return db if not formato else moeda(db)


def metade(valor=0, formato=False):
    m = valor / 2
    return m if not formato else moeda(m)


def moeda(valor=0, moeda= 'R$'):
    return f'{moeda} {valor:>.2f}'.replace('.', ',')


