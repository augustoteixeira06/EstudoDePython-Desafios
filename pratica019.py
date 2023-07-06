# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.Faça um programa que ajude ele, lendo o nome deles eescrevendo o nome do escolhido.
import random
n1 = str(input('Digite o nome do primeiro aluno:'))
n2 = str(input('Digite o nome do segundo aluno:'))
n3 = str(input('Digite o nome do terceiro aluno:'))
n4 = str(input('Digite o nome do quarto aluno:'))
lista = [n1, n2, n3, n4]
# A função CHOICE precisa de uma lista com os elementos. Listas precisam ficar entre colchetes.
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
