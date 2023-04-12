num = list()

while True:
    num.append(int(input('Digite um valor: ')))

    r = str(input('Quer continuar: [S/N] '))

    if r in 'Nn':
        print('Finalizando...')
        break

print('-=' * 30)
print(f'Você digitou {len(num)} elementos')
num.sort(reverse=True)
print(f'Os valores em ordem descrescente são {num}')
if 5 in num:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')