from random import randint
computador = randint(0, 10)
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi? ''')
jogador = int(input('Qual o seu palpite? '))
tentativa = 1
while jogador != computador:
    if jogador > computador:
        print('Informe um número menor... ')
    elif jogador < computador:
        print('Informe um número maior... ')
    jogador = int(input('Tente novamente: '))
    tentativa += 1
print(f'Parabéns. Você venceu com {tentativa} tentativas. ')
