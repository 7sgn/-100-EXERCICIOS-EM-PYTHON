n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f} o aluno fica com média {:.1f}'.format(n1, n2, media))

if media <= 5.0:
    print('O aluno está REPROVADO!')
elif media > 5.0 and media < 6.9:
    print('O aluno está de RECUPERAÇÃO!')
elif media >= 7:
    print('O aluno está APROVADO!')