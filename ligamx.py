import random
import pandas as pd
import numpy as np
from scipy.stats import poisson 
from matplotlib import pyplot as plt
import seaborn as sns
import re
import lxml

data = pd.read_html('https://www.espn.com.mx/futbol/posiciones/_/liga/mex.1',encoding='UTF-8')
calendario=pd.read_csv('CALENDARIO.csv')
local=calendario.LOCAL[0:153]
visita=calendario.VISITA[0:153]

tabla=data[1]
equipo=data[0]
equipo=['América','Atlas','Atlético de San Luis','Tijuana','Cruz Azul','Guadalajara','FC Juarez','León','Mazatlán FC','Monterrey','Necaxa','Pachuca','Puebla','Pumas UNAM','Querétaro','Santos','Tigres UANL','Toluca']
tabla.index=equipo
GF_promedio=tabla.GF/tabla.J
GC_promedio=tabla.GC/tabla.J
goles_promedio_ligamx=tabla.GF.mean()
ataque=GF_promedio/goles_promedio_ligamx
defensa=GC_promedio/goles_promedio_ligamx

df=pd.DataFrame({'Juegos':tabla.J,'Ganados':tabla.G, 'Perdidos':tabla.P, 'Empates':tabla.E,'GF promedio':GF_promedio, 'GC promedio':GC_promedio,'Ataque':ataque,'Defensa':defensa})

games=pd.DataFrame({'LOCAL':local.to_list(),'goles local':np.random.randint(low = 0,high=7,size=153) ,'VISITA':visita.to_list(), 'goles visita':np.random.randint(low = 0,high=7,size=153)})

G=(games['goles local']>games['goles visita'])
P=(games['goles local']<games['goles visita'])
E=(games['goles local']==games['goles visita'])
games['G']=G.astype(int)
games['P']=P.astype(int)
games['E']=E.astype(int)

print(games)
