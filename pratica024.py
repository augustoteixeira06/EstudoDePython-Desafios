# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
cid = str(input('Digite o nome da cidade:')).strip()
print(cid[:5].upper() == 'SANTO')
# O strip no início serve para ignorar os 'espaços' digitados antes ou depois.
# Analisar a primeira palavra digitada do elemento 0 até o quinto ([0:5] ou [:5] dá no mesmo), jogar tudo pra maiúsculas (upper) e igualar (==) com a palavra "SANTO" em maiúscula, para exibir "verdadeiro" ou "falso".
