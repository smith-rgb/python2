import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Cargar el archivo CSV

df = pd.read_csv('poblacion.csv')


# Seleccionar algunos países para visualizar
paises = ['ARG', 'BRA', 'CHL', 'COL', 'AZE']

# Filtrar el DataFrame
df_filtrado = df[['Date'] + paises]

plt.figure(figsize=(8, 6))
sns.lineplot(data=df_filtrado, linewidth=3)
plt.title('Evolución de la Población por País (Seaborn)')
plt.xlabel('Año')
plt.ylabel('Población')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()