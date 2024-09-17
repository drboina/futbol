import pandas as pd

jornada = 7
def clean_tabla():
    tabla = pd.read_html("https://mexico.as.com/resultados/futbol/mexico_apertura/clasificacion/", encoding='UTF-8')
    tabla = tabla[1]
    club = tabla['Equipo'].str.split("  ").str[-1]
    tabla.Equipo = club
    tabla.index = club  
    return tabla

tabla = clean_tabla()
prom = tabla.GF.sum()/tabla.PJ.sum()
def juegos(jornada):
    game = pd.read_html("https://mexico.as.com/resultados/futbol/mexico_apertura/calendario/", encoding='UTF-8')
    return game[jornada]

partidos = juegos(jornada)
def listas(tabla, partidos, prom):
    tabla['Ataque'] = (tabla.GF/tabla.PJ)/prom
    tabla['Defensa'] = (tabla.GC/tabla.PJ)/prom
    equipo_local = partidos['Equipo local'].to_list()
    equipo_visita = partidos['Equipo visitante'].to_list()
    return tabla, equipo_local, equipo_visita

[tabla, equipo_local, equipo_visita] = listas(tabla, partidos, prom)
def xG(equipo_local, equipo_visita):

    def multiplicar_elementos(lista1, lista2, prom):
        return [lista1[i] * lista2[i] * prom for i in range(len(lista1))]
    
    def restar_elementos(lista1,lista2):
        return [lista1[i] - lista2[i] for i in range(len(lista1))]
    
    ataque_local = tabla.Ataque[equipo_local].to_list()
    defensa_local = tabla.Defensa[equipo_local].to_list()
    ataque_visita = tabla.Ataque[equipo_visita].to_list()
    defensa_visita = tabla.Defensa[equipo_visita].to_list()

    xG_local = multiplicar_elementos(ataque_local, defensa_visita, prom)
    xG_visita = multiplicar_elementos(ataque_visita, defensa_local, prom)
    dif = restar_elementos(xG_local,xG_visita)
    return xG_local, xG_visita, dif

xG_local, xG_visita, dif = xG(equipo_local, equipo_visita)

pronostico = pd.DataFrame({"Equipo Local":tabla.Equipo[equipo_local].to_list(),"xG_local":xG_local,"xG_visita":xG_visita,"Equipo Visita":tabla.Equipo[equipo_visita].to_list(), 'dif': dif})
def save(tabla, pronostico, partidos, jornada):
    pronostico.to_csv(f"pronostico_jornada_{jornada}.csv")
    partidos.to_csv(f"partidos_jornada_{jornada}.csv")
    print("\n",tabla.sort_values('Pts.', ascending=False).to_string(index=False))
    print("\n",partidos.to_string(index=False))
    print("\n",pronostico.to_string(index=False))
 
save(tabla, pronostico, partidos, jornada)
