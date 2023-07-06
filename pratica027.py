# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome separadamente.
n = str(input('Digite seu nome completo:')).strip()
nome = n.split()
# função split para separar os elementos do nome em lista
print('Prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
# [0] para mostrar o elemento digitado na primeira posição, que é zero
print('Seu último nome é {}'.format(nome[len(nome)-1]))
# o len serve para contar quantos elementos tem o nome digitado, pardindo do zero.

# Mostrar nome na posição len de nome. O -1 serve para mostrar o elemento na última posição.
