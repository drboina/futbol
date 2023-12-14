import pandas as pd
import numpy as np
from scipy.stats import poisson 
from matplotlib import pyplot as plt
import seaborn as sns
import re

tabla = pd.read_html('https://www.espn.com.mx/futbol/posiciones/_/liga/mex.1',encoding='UTF-8')
tabla=tabla[1]
equipo=['América','Monterrey','Tigres UANL','Pumas UNAM','Guadalajara','Puebla','Atlético de San Luis','León','Santos','Mazatlán','Pachuca','Toluca','Tijuana','Querétaro','FC Juarez','Cruz Azul','Atlas','Necaxa']

tabla.index=equipo
GF_promedio=tabla.GF/tabla.J
GC_promedio=tabla.GC/tabla.J
goles_promedio_ligamx=tabla.GF.mean()
ataque=GF_promedio/goles_promedio_ligamx
defensa=GC_promedio/goles_promedio_ligamx

df=pd.DataFrame({'Juegos':tabla.J,'Ganados':tabla.G, 'Perdidos':tabla.P, 'Empates':tabla.E,'GF promedio':GF_promedio, 'GC promedio':GC_promedio,'Ataque':ataque,'Defensa':defensa})

print(df)
