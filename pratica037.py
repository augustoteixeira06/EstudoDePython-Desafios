# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção:'))
if opção == 1:
    print('O valor {} convertido para BINÁRIO é {}'.format(num, bin(num)[2:]))
# O Python tem um recurso de conversão. Bin para binário, oct para octal, hex para hexadecimal.
elif opção == 2:
    print('O valor {} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('O valor {} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
# O Python tem um código para cada conversão. 0b para binário, 0o para octal e 0x para hexadecimal. Para retirar essa infomação basta usar o recurso de fateamento. entre [] dois para mostrar a informação depois do segundo caractere e : para ir até o final da string.
else:
    print('Opção inválida. Tente novamente.')
