import pandas as pd

jornada = 7
gol = pd.DataFrame()
for i in range(1,jornada+1) : gol = pd.read_csv(f'pronostico_jormada_{i}.csv', encoding='UTF-8')
print(gol)