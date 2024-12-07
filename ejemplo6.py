import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
# Cargar el archivo CSV

df=pd.read_csv("poblacion.csv")

#seleccionar algunos paises para visualizar 
paises=["GEO", "GRL", "GUM", "GUY", "HIC"]

#filtrar el dataframe 
df_filtrado= df [["Date"]+ paises]

plt.figure(figsize=(8, 6))
sns.lineplot(data=df_filtrado, linewidth=3)
plt.title("evolucion de la poblacion por pais (seaborn")
plt.xlabel("año")
plt.ylabel("poblacion")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()