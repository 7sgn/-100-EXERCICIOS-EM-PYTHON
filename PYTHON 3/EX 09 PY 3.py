num = list()
par = list()
impar = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Deseja continuar? '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print('-=' * 30)
impar.sort()
num.sort()
par.sort()
print(f'A lista completa é {num}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')


