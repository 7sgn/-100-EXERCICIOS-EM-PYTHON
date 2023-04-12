preço = float(input('Digite o valor do produto: '))
desconto = preço - (preço * 0.05)
print('O valor do produto é R${}, com desconto de 5% fica R${} reais. '.format(preço, desconto))
