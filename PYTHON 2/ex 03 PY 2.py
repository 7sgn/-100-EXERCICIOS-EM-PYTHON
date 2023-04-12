a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
if a > b:
    print('O número {} é maior do que {}'.format(a,b))
elif b > a:
    print('O número {} é maior que o {}'.format(b,a))
else:
    print('Os dois valores são IGUAIS')