import pandas as pd

def clean_data():
    tabla = pd.read_html("https://www.goal.com/es-mx/noticias/tabla-general-liga-mx/gotsl4uias0z1nyvu8pktnv1b",encoding='UTF-8')
    club = tabla[0]
    club = club[1]
    club = club[1:]
    tabla = pd.read_html("https://espndeportes.espn.com/futbol/posiciones/_/liga/mex.1/liga-mx", encoding='UTF-8')
    tabla = tabla[1]
    club.index = tabla.index
    tabla['Club'] = club
    tabla = pd.DataFrame({'Club': club, 'Ataque':(tabla.GF/tabla.J)/(tabla.GF.sum()/tabla.J.sum()), 'Defensa': (tabla.GC/tabla.J)/(tabla.GF.sum()/tabla.J.sum()), 'J': tabla.J, 'GF': tabla.GF, 'GC': tabla.GC})
    return tabla

tabla = clean_data()
print(f'{tabla}\n')

def promedio():
    promedio = tabla.GF.sum()/tabla.J.sum()
    print(f'No. goles promedio en liga: {promedio}\n')
    return promedio

goles_prom_liga = promedio()

def multiplicar_elementos(lista1, lista2):
    return [lista1[i] * lista2[i] for i in range(len(lista1))]

local = [16,14,1,0,4,10,13,6,17]
visita = [5,15,12,9,2,3,7,8,11]

ataque_local = tabla.Ataque[local].to_list()
defensa_local = tabla.Defensa[local].to_list()
ataque_visita = tabla.Ataque[visita].to_list()
defensa_visita = tabla.Defensa[visita].to_list()

xG_local = multiplicar_elementos(ataque_local, defensa_visita)
xG_visita = multiplicar_elementos(ataque_visita, defensa_local)

for i in range(len(xG_local)):
    print(f'{tabla.Club[local[i]]}:{xG_local[i]} \nvs\n{tabla.Club[visita[i]]}:{xG_visita[i]}\n')
