# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 85km/h mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 para cara KM acima do limite.
vel = float(input('Qual é a velocidade atual do carro? '))
if vel > 80:
    print('\033[31mMULTADO! Você excedeu o limite permitido, que é de 80km/h! ')
    multa = (vel-80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}!\033[m ')
print('\033[33mTenha um boa dia! Dirija com segurança! ')
