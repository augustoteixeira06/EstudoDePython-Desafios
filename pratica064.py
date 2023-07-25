# Programa para ler vários números inteiros e mostrar a soma entre eles.
# Criar uma condição de parada.
n = cont = soma = 0
# Maneira simplificada de digitar  n = 0, cont = 0 e soma = 0.
n = int(input('Digite um número [999 para parar] '))
# Lendo o flag do lado de fora. Assim ele não é somado.
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 para parar] '))
    # Se n for igual a 999 ele sairá do loop e não somará.
print(f'Você digitou {cont} números e a soma entre eles foi {soma}. ')

