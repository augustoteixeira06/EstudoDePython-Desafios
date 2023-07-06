# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
# MEU CÓDIGO:
'''import random
n = int(input('Advinhe o número que estou pensando:'))
nc = random.randint(0, 5)
if n == nc:
    print('Parabéns, você acertou! Pensei realmente no número {}'.format(nc))
else:
    print('Que pena, você errou... Na verdade pensei no número {}'.format(nc))'''

#CÓDIGO DO PROFESSOR:
import random
import time
computador = random.randint(0, 5)
# randint para fazer o programa escolher um número aleatório entre 0 e 5
print('-=-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-=-' * 20)
jogador = int(input('Em que número estou pensando?'))
print('PROCESSANDO...')
time.sleep(1)
# sleep para aguardar 2 segundos na mensagem
if jogador == computador:
    print('\033[34mPARABÉNS! Você conseguiu me vencer!')
else:
    print('\033[31mQue pena... você PERDEU! Na verdade pensei em {} e não em {}.'.format(computador, jogador))
