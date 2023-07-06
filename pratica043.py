# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
# e mostre seu status, de acordo com a tabela a seguir: - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal - 25 até 30: Sobrepeso - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida.
peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O seu IMC é de {:.1f} '.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso ideal. ')
elif imc >= 18.5 and imc < 25:
    print('Você está na faixa de peso IDEAL. ')
elif imc >= 25 and imc < 30:
    print('Você está com SOBREPESO! ')
elif imc >= 30 and imc < 40:
    print('Você está em OBESIDADE! ')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado! ')

'''peso = float(input('Qual é o seu peso? (kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print(f'O seu IMC é {imc:.1f}. ')
if imc < 18.5:
    print('Você está abaixo do peso. ')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal. ')
elif 25 <= imc < 30:
    print('Você está acima do peso. ')
elif 30 <= imc < 40:
    print('CUIDADO! Você está em obesidade. ')
else:
    print('MUITO CUIDADO! Você tem obesidade mórbida! Procure um médico.')'''