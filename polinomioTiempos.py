import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/edtrelo/TMI/main/respuestas_encuesta_tmi.csv', sep = ',')

# obtenemos las observaciones de los tiempos de traslado
tiempos = np.sort(data['Tiempo Total'].unique())

# sacamos la media de los promedios para cada observación de tiempo
mean_promedios = data.groupby('Tiempo Total')['Promedio'].mean().array

# obtenemos los parámetros que mejor se ajustan con un polinomio de grado 9
params = np.polyfit(tiempos, means_prom, 9)

print(params)

# los parámetros obtenidos son: 
# [-9.75115667e-18  1.00826570e-14 -3.93837327e-12  7.54756188e-10 -7.40380028e-08  3.26389292e-06 -1.89153627e-05 -1.89163893e-03 -1.20437758e-02  9.40462541e+00]
