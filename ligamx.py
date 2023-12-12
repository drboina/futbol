import pandas as pd
import numpy as np
from scipy.stats import poisson 
from matplotlib import pyplot as plt
import seaborn as sns

tabla = pd.read_html('https://www.espn.com.mx/futbol/posiciones/_/liga/mex.1',encoding='UTF-8')
equipo=tabla[0]
tabla=tabla[1]
print(equipo)
print(tabla)
