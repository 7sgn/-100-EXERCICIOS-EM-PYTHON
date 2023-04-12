totP = 0
while True:
    produto = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o valor do produto: '))

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
