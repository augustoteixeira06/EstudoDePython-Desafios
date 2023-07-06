# Crie um programa que faça o computador jogar Jokenpô com você
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas escolhas:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Escolha é a sua jogada: '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!!')
print('-=' * 15)
print('O jogador escolheu: {}'.format(itens[jogador]))
print('O computador escolheu: {}'.format(itens[computador]))
print('-=' * 15)
if computador == 0:
    if jogador == 0:
        print('EMPATE! ')
    elif jogador == 1:
        print('O COMPUTADOR VENCEU DESSA VEZ. ')
    elif jogador == 2:
        print('O JOGADOR VENCEU. PARABÉNS!')
elif computador == 1:
    if jogador == 0:
        print('O JOGADOR VENCEU. PARABÉNS! ')
    elif jogador == 1:
        print('EMPATE! ')
    elif jogador == 2:
        print('O COMPUTADOR VENCEU DESSA VEZ. ')
elif computador == 2:
    if jogador == 0:
        print('O COMPUTADOR VENCEU DESSA VEZ. ')
    elif jogador == 1:
        print('O JOGADOR VENCEU. PARABÉNS! ')
    elif jogador == 2:
        print('EMPATE!')
