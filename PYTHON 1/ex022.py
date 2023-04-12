
'''CRIE UM PROGRAMA QUE LEIA O OME COMPLETO DE UMA PESSOA E MOSTRE:
- O NOME COM TODAS AS LETRAS AMIUSCULAS E MINUSCULAS
- QUANTAS LETRAS AO TODO (SEM CONSIDERAR ESPAÇOS)
- QUANTAS LETRAS TEM O PRIMEIRO NOME'''



nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Sei primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
