# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: - Média abaixo de 5.0: REPROVADO - Média entre 5.0 e 6.9: RECUPERAÇÃO - Média 7.0 ou superior: APROVADO
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('A média do aluno foi {:.1f} '.format(media))
if media < 5:
    print('Com essa média o aluno está REPROVADO! ')
elif media >= 5 and media <= 6.9:
    print('Com essa média o aluno está em RECUPERAÇÃO! ')
elif media >= 7.0:
    print('Com essa média o aluno está APROVADO! ')



'''av1 = float(input('Primeira nota: '))
av2 = float(input('Segunda nota: '))
media = (av1 + av2) / 2
print(f'Tirando {av1:.1f} e {av2:.1f}, a média do aluno é {media:.1f}. ')
if media >= 7:
   print('O aluno está APROVADO! ')
elif media < 6.9 and media >= 5:
    print('O aluno está em RECUPERAÇÃO! ')
elif media < 5:
    print('O aluno está REPROVADO! ')'''
