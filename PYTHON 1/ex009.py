valor = float(input('Digite um valor em R$: '))
dol = valor / 4.9592007
print('Com R${} reais você pode comprar U$${:.2f} dólares.'.format(valor, dol))