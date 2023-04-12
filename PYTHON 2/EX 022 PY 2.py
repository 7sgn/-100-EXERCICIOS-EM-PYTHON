from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print(''' 
     [ 1 ] somar
     [ 2 ] multiplicar
     [ 3 ] maior
     [ 4 ] novos números
     [ 5 ] sair do programa''')
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1,n2,soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1,n2,produto))
    elif opção == 3:
        if n2 > n2:
            maior = n1
            print('O maior número é {}'.format(n1))
        else:
            maior = n2
            print('O maior número é {}'.format(n2))
    elif opção == 4:
        print('Digite os números novamente')
        n1 = int(input('Primeiro Número: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa')