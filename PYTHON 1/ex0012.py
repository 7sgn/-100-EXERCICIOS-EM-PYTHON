salario = float(input('Digite o valor do salário:'))
novo = salario + (salario*15/100)
print('O salário do funcionário que era R${} após o reajuste de 15% passou a ser R${}.'.format(salario, novo))