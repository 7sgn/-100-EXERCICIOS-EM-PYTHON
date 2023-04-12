#km = float(input('Digite a distância em km/h: '))
#if km < 200:
 #   preco = km * 0.50
#else:
 #   preco = km * 0.45
#print('O preço da sua passagem é de: {:.2f}'.format(preco))


distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format (preço))