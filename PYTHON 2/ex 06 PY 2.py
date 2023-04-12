from datetime import date
nasc = int(input('Seu ano de nascimento: '))
atual = date.today().year
idade = (atual - nasc)
print('Se você nasceu em {} sua idade é {}'.format(nasc, idade))

