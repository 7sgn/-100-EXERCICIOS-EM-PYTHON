valor = []
mai = 0
men = 0
for c in range(0, 5):
    valor.append(input(f'Digite um número na posição {c}: '))
    if c == 0:
        mai = men = valor[c]
    else:
        if valor[c] > mai:
            mai = valor[c]
        if valor[c] < men:
            men = valor[c]
print('=-' * 30)
print(f'Você digitou os números: {valor}')
print(f'O maior valor foi `{mai} na posição ', end='')
for i, v in enumerate(valor):
    if v == mai:
        print(f'{i}...', end='')
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(valor):
    if v == men:
        print(f'{i}...', end='')





