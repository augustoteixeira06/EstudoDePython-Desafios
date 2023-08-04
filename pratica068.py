# Programa de jogo par ou ímpar com o computador. O jogo será interrompido quando o jogador
# perder, mostrando o total de vitórias consecutivas do jogador no final.

 random import randint
v = 0
while True:
    jogador = int(input('Digite um número para jogar: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou ÍMPAR? [P/I] ')).strip().upper()[0]
# Strip para remover espaços, upper para maiúsculas e [0] para checar a primeira letra.
    print(f'O jogador jogou {jogador} e o computador {computador}. Total igual a {total}. ', end='')
    print('DEU PAR!' if total % 2 == 0 else 'DEU ÍMPAR! ')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu! ')
            v = v + 1
        else:
            print('Você perdeu! ')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu! ')
            v = v + 1
        else:
            print('Você perdeu! ')
            break
    print('Vamos jogar novamente... ')
print(f'GAME OVER! Você venceu {v} vezes. ')
