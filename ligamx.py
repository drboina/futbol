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
print(tabla)