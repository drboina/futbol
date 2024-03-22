import pandas as pd
import numpy as np
from datetime import datetime

def current_date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = "{} de {} del {}".format(day, month, year)

    return messsage

now = datetime.now()
print('\n')
print(current_date_format(now))

equipos = pd.read_html("https://www.goal.com/es-mx/noticias/tabla-general-liga-mx/gotsl4uias0z1nyvu8pktnv1b",encoding='UTF-8')
equipo = equipos[0]
team = equipo[1]
club = team[1:]
tabla_gral = pd.read_html("https://espndeportes.espn.com/futbol/posiciones/_/liga/mex.1/liga-mx", encoding='UTF-8')
tabla = tabla_gral[1]
club.index = tabla.index
tabla['Club'] = club

tabla2=pd.DataFrame()
tabla2['Club'] = club
tabla2['Ataque'] = (tabla.GF/tabla.J)/(tabla.GF.sum()/tabla.J.sum())
tabla2['Defensa'] = (tabla.GC/tabla.J)/(tabla.GF.sum()/tabla.J.sum())

print('\n')
print(tabla2)
print('\nLiga mx')
print(f'Goles promedio: {tabla.GF.sum()/tabla.J.sum()}')

x=[0,5,7,9]
y=[4,3,1,6]
i=1
while i<len(x): 
    Gx=tabla2.loc[x[i]]["Ataque"]*tabla2.loc[y[i]]["Defensa"]*(tabla.GF.sum()/tabla.J.sum())
    print(f'\n{tabla2.loc[x[i]]["Club"]}: {Gx}')
    Gy=tabla2.loc[y[i]]["Ataque"]*tabla2.loc[x[i]]["Defensa"]*(tabla.GF.sum()/tabla.J.sum())
    print(f'{tabla2.loc[y[i]]["Club"]}: {Gy}')
    i=i+1
