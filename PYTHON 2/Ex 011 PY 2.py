soma = 0    # acumulador
cont = 0    # Somador
for c in range (1,501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))