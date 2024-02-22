import pandas as pd

#Limpieza y tratamiento de datos
equipos = pd.read_html("https://www.goal.com/es-mx/noticias/tabla-general-liga-mx/gotsl4uias0z1nyvu8pktnv1b",encoding='UTF-8')
equipo = equipos[0]
team = equipo[1]
club = team[1:]

tabla_gral = pd.read_html("https://espndeportes.espn.com/futbol/posiciones/_/liga/mex.1/liga-mx", encoding='UTF-8')
tabla = tabla_gral[1]
club.index = tabla.index
tabla['Club'] = club

calendario=pd.read_csv('CALENDARIO.csv')
index = calendario['FECHA'][60:81]
local = str(calendario['LOCAL'][60:70])
visita = str(calendario['VISITA'][60:70])

#Cálculos estadisticos
GF_promedio=tabla.GF/tabla.J
GC_promedio=tabla.GC/tabla.J
goles_promedio_ligamx=tabla.GF.sum()/tabla.J.sum()
ataque=GF_promedio/goles_promedio_ligamx
defensa=GC_promedio/goles_promedio_ligamx
tabla['Ataque'] = ataque
tabla['GF_promedio'] = GF_promedio
tabla['Defensa'] = defensa
tabla['GC_promedio'] = GC_promedio

#Display de resultados
print(f'\n goles promedio de ligamx: {goles_promedio_ligamx} por partido\n')
print(tabla)
print('\n')
print(f'{tabla.loc[15]["Club"]}: {tabla.loc[15]["Ataque"]*tabla.loc[3]["Defensa"]*goles_promedio_ligamx}')
print('vs')
print(f'{tabla.loc[3]["Club"]}: {tabla.loc[3]["Ataque"]*tabla.loc[15]["Defensa"]*goles_promedio_ligamx}')
print('\n')
print(f'{tabla.loc[7]["Club"]}: {tabla.loc[7]["Ataque"]*tabla.loc[6]["Defensa"]*goles_promedio_ligamx}')
print('vs')
print(f'{tabla.loc[6]["Club"]}: {tabla.loc[6]["Ataque"]*tabla.loc[7]["Defensa"]*goles_promedio_ligamx}')
print('\n')
print(f'{tabla.loc[8]["Club"]}: {tabla.loc[8]["Ataque"]*tabla.loc[16]["Defensa"]*goles_promedio_ligamx}')
print('vs')
print(f'{tabla.loc[16]["Club"]}: {tabla.loc[16]["Ataque"]*tabla.loc[8]["Defensa"]*goles_promedio_ligamx}')
print('\n')
print(f'{tabla.loc[4]["Club"]}: {tabla.loc[4]["Ataque"]*tabla.loc[12]["Defensa"]*goles_promedio_ligamx}')
print('vs')
print(f'{tabla.loc[12]["Club"]}: {tabla.loc[12]["Ataque"]*tabla.loc[4]["Defensa"]*goles_promedio_ligamx}')
print('\n')
print(f'{tabla.loc[10]["Club"]}: {tabla.loc[10]["Ataque"]*tabla.loc[0]["Defensa"]*goles_promedio_ligamx}')
print('vs')
print(f'{tabla.loc[0]["Club"]}: {tabla.loc[0]["Ataque"]*tabla.loc[10]["Defensa"]*goles_promedio_ligamx}')
print('\n')