#Faça um programa que lea uma frase e mostre: 
# - Quantas vezes aparece a letra "A"
# - Em que posição ela aparece pela primeira vez
# - Em que posição ela aparece pela última vez
frase = str(input('Digite uma frase:')).upper().strip()
# upper pra jogar tudo pra maiúsculas e auxiliar no count e strip pra náo contar os espaços entre as palavras
print('A letra "A" aparece {} vezes'.format(frase.count('A')))
# count conta quantas vezes a letra aparece
print('A primeira letra "A" aparece na posição {}'.format(frase.find('A')))
# find procura a primeira letra definida na frase da ordem normal
print('A última letra "A" aparece na posição {}'.format(frase.rfind('A')))
# rfind procura a primeira letra da direita para a esquerda
