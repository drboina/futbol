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

def promedio_goles():
    promedio = tabla.GF.sum()/tabla.J.sum()
    return promedio

goles_prom_liga = promedio_goles()

def multiplicar_elementos(lista1, lista2):
    return [lista1[i] * lista2[i] * goles_prom_liga for i in range(len(lista1))]

def juegos(jornada):
    game = pd.read_html("https://mexico.as.com/resultados/futbol/mexico_apertura/calendario/", encoding='UTF-8')
    return game[jornada]

jornada = 4
partidos = juegos(jornada)
print("\n",partidos.iloc[:])

local = [17,16,7,10,5,13,3,8,4]
visita = [1,11,0,14,2,15,6,12,9]

ataque_local = tabla.Ataque[local].to_list()
defensa_local = tabla.Defensa[local].to_list()
ataque_visita = tabla.Ataque[visita].to_list()
defensa_visita = tabla.Defensa[visita].to_list()

xG_local = multiplicar_elementos(ataque_local, defensa_visita)
xG_visita = multiplicar_elementos(ataque_visita, defensa_local)

pronostico = pd.DataFrame({"Local":tabla.Club[local].to_list(),"xG_local":xG_local,"Visita":tabla.Club[visita].to_list(),"xG_visita":xG_visita})
print("\n",pronostico)
pronostico.to_csv(f"pronostico_jormada_{jornada}.csv")
        

