salario = float(input('Digite seu salário: '))
if salario > 1.250:
    novo = salario + (salario * 0.10)
if salario < 1.250:
    novo = salario + (salario * 0.15)
print('Seu salário era {}  e passou a ser {} após o reajuste.'.format(salario,novo))
