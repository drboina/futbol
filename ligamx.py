import pandas as pd

jornada = int(input("No. de la jornada: "))

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

def juegos(jornada):
    game = pd.read_html("https://mexico.as.com/resultados/futbol/mexico_apertura/calendario/", encoding='UTF-8')
    return game[jornada]

partidos = juegos(jornada)
resultados = juegos(jornada-1)

def promedio_goles():
    promedio = tabla.GF.sum()/tabla.J.sum()
    return promedio

goles_prom_liga = promedio_goles()

def multiplicar_elementos(lista1, lista2):
    return [lista1[i] * lista2[i] * goles_prom_liga for i in range(len(lista1))]

def juegos(jornada):
    game = pd.read_html("https://mexico.as.com/resultados/futbol/mexico_apertura/calendario/", encoding='UTF-8')
    return game[jornada]

partidos = juegos(jornada)
resultados = juegos(jornada-1)

local = [4,7,11,14,17,10,6,12,5]
visita = [13,11,3,2,0,8,15,9,16]

def xG(local,visita):
    ataque_local = tabla.Ataque[local].to_list()
    defensa_local = tabla.Defensa[local].to_list()
    ataque_visita = tabla.Ataque[visita].to_list()
    defensa_visita = tabla.Defensa[visita].to_list()
    return [ataque_local, ataque_visita, defensa_local, defensa_visita]

[ataque_local, ataque_visita, defensa_local, defensa_visita] = xG(local,visita)

xG_local = multiplicar_elementos(ataque_local, defensa_visita)
xG_visita = multiplicar_elementos(ataque_visita, defensa_local)

pronostico = pd.DataFrame({"Local":tabla.Club[local].to_list(),"xG_local":xG_local,"xG_visita":xG_visita,"Visita":tabla.Club[visita].to_list()})
pronostico.to_csv(f"pronostico_jormada_{jornada}.csv")
resultados.to_csv(f"resultados_jornada_{jornada-1}.csv")
print(f'\n{tabla}\n')
print("\n",resultados)
print("\n",pronostico)
print("\n",partidos)

        

