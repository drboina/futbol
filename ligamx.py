import pandas as pd
import numpy as np
from scipy.stats import poisson 
from matplotlib import pyplot as plt
import seaborn as sns
import re
import lxml
from datetime import datetime

def current_date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = "{} de {} del {}".format(day, month, year)

    return messsage

now = datetime.now()

#Limpieza y tratamiento de datos
equipos = pd.read_html("https://www.goal.com/es-mx/noticias/tabla-general-liga-mx/gotsl4uias0z1nyvu8pktnv1b",encoding='UTF-8')
equipo = equipos[0]
team = equipo[1]
club = team[1:]

tabla_gral = pd.read_html("https://espndeportes.espn.com/futbol/posiciones/_/liga/mex.1/liga-mx", encoding='UTF-8')
tabla = tabla_gral[1]
club.index = tabla.index
tabla['Club'] = club
tabla2=pd.DataFrame()
#Cálculos estadisticos
GF_promedio=tabla.GF/tabla.J
GC_promedio=tabla.GC/tabla.J
goles_promedio_ligamx=tabla.GF.sum()/tabla.J.sum()
ataque=GF_promedio/goles_promedio_ligamx
defensa=GC_promedio/goles_promedio_ligamx
tabla2['Club'] = club
tabla2['Ataque'] = ataque
tabla2['GF_promedio'] = GF_promedio
tabla2['Defensa'] = defensa
tabla2['GC_promedio'] = GC_promedio

#
print(tabla2)
print(current_date_format(now))

print('Jornada 11 de 17 - Liga Mx')
print(f'\nGoles promedio: {goles_promedio_ligamx} por partido\n')

print(f'{tabla2.loc[9]["Club"]}: {tabla2.loc[9]["Ataque"]*tabla2.loc[17]["Defensa"]*goles_promedio_ligamx}')
print(f'{tabla2.loc[17]["Club"]}: {tabla2.loc[17]["Ataque"]*tabla2.loc[9]["Defensa"]*goles_promedio_ligamx}')
print('\n')

print(f'{tabla2.loc[2]["Club"]}: {tabla2.loc[2]["Ataque"]*tabla2.loc[5]["Defensa"]*goles_promedio_ligamx}')
print(f'{tabla2.loc[5]["Club"]}: {tabla2.loc[5]["Ataque"]*tabla2.loc[2]["Defensa"]*goles_promedio_ligamx}')
print('\n')

print(f'{tabla2.loc[10]["Club"]}: {tabla2.loc[10]["Ataque"]*tabla2.loc[16]["Defensa"]*goles_promedio_ligamx}')
print(f'{tabla2.loc[16]["Club"]}: {tabla2.loc[16]["Ataque"]*tabla2.loc[10]["Defensa"]*goles_promedio_ligamx}')
print('\n')

print(f'{tabla2.loc[12]["Club"]}: {tabla2.loc[12]["Ataque"]*tabla2.loc[0]["Defensa"]*goles_promedio_ligamx}')
print(f'{tabla2.loc[0]["Club"]}: {tabla2.loc[0]["Ataque"]*tabla2.loc[12]["Defensa"]*goles_promedio_ligamx}')
print('\n')

print(f'{tabla2.loc[4]["Club"]}: {tabla2.loc[4]["Ataque"]*tabla2.loc[7]["Defensa"]*goles_promedio_ligamx}')
print(f'{tabla2.loc[7]["Club"]}: {tabla2.loc[7]["Ataque"]*tabla2.loc[4]["Defensa"]*goles_promedio_ligamx}')
print('\n')

print(f'{tabla2.loc[15]["Club"]}: {tabla2.loc[15]["Ataque"]*tabla2.loc[11]["Defensa"]*goles_promedio_ligamx}')
print(f'{tabla2.loc[11]["Club"]}: {tabla2.loc[11]["Ataque"]*tabla2.loc[15]["Defensa"]*goles_promedio_ligamx}')
print('\n')

print(f'{tabla2.loc[6]["Club"]}: {tabla2.loc[6]["Ataque"]*tabla2.loc[14]["Defensa"]*goles_promedio_ligamx}')
print(f'{tabla2.loc[14]["Club"]}: {tabla2.loc[14]["Ataque"]*tabla2.loc[6]["Defensa"]*goles_promedio_ligamx}')
print('\n')

print(f'{tabla2.loc[8]["Club"]}: {tabla2.loc[8]["Ataque"]*tabla2.loc[1]["Defensa"]*goles_promedio_ligamx}')
print(f'{tabla2.loc[1]["Club"]}: {tabla2.loc[1]["Ataque"]*tabla2.loc[8]["Defensa"]*goles_promedio_ligamx}')
print('\n')

print(f'{tabla2.loc[13]["Club"]}: {tabla2.loc[13]["Ataque"]*tabla2.loc[3]["Defensa"]*goles_promedio_ligamx}')
print(f'{tabla2.loc[3]["Club"]}: {tabla2.loc[3]["Ataque"]*tabla2.loc[13]["Defensa"]*goles_promedio_ligamx}')
print('\n')


