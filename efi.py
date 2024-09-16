import pandas as pd

jornada = range(1,8)
print(jornada)
pronosticos = pd.read_csv('pronostico_jormada_0.csv', encoding='UTF-8')
resultados = pd.read_csv('partidos_jornada_0.csv', encoding='UTF-8')

for i in jornada: pronosticos = pd.concat([pronosticos, pd.read_csv(f'pronostico_jormada_{i}.csv', encoding='UTF-8')])
for i in jornada: resultados = pd.concat([resultados, pd.read_csv(f'partidos_jornada_{i}.csv', encoding='UTF-8')])

resultados = resultados.Resultado.str.split(' - ')
pronosticos.drop('Unnamed: 0', axis=1)

print(len(resultados))
print(len(pronosticos))
