# Programa para mostrar a tabela do Campeonato Brasileiro: Os 5 primeiros,
# os últimos 4, ordem alfabética e posição do time do Fortaleza.
times = ('Botafogo', 'Flamengo', 'Fluminense', 'Palmeiras', 'Bragantino',
         'Grêmio', 'Athletico-PR', 'Cuiabá', 'São Paulo', 'Atlético-MG',
         'Cruzeiro', 'Internacional', 'Fortaleza', 'Corintians', 'Goiás',
         'Bahia', 'Santos', 'Coritiba', 'Vasco da Gama', 'América-MG')
print('-*-'*30)
print(f'Times do Campeonato Brasileiro: {times}')
print('-*-'*30)
print(f'Os 4 primeiros colocados: {times[0:4]}')
print('-*-'*30)
print(f'BÔNUS! Times em ordem alfabética: {times[-4:]}')
# -4 significa contar a tupla de trás para frente. Do elemento -4 até o fim da tupla.
print('-*-'*30)
