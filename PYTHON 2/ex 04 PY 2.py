from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
print('''Informe o seu sexo: 
[ 1 ] Masculino
[ 2 ] Feminino    ''')
opcao = int(input('Escolha sua opção: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18 and opcao == 1:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade > 18 and opcao == 1:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
elif idade < 18 and opcao == 1:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade == 18 and opcao == 2:
    print('Você pode se alistar esse ano, no entanto o seu alistamento não é obrigatório')
elif idade > 18 and opcao == 2:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    print('Seu alistamento não é Obrigatório')
elif idade < 18 and opcao == 2:
    print('Ainda faltam {} anos para seu alistamento, no entanto ele não é obrigatório')


