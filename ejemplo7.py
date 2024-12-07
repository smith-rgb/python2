import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
# Cargar el archivo CSV

df=pd.read_csv("poblacion.csv")

#seleccionar algunos paises para visualizar 
paises=["GEO", "GRL", "GUM", "GUY", "HIC"]


# Datos de ejemplo
df_filtrado= df [["Date"]+ paises]
# Crear gráfico circular
plt.pie(paises, labels=categorias, autopct="%1.1f%%", startangle=140)
plt.title("Gráfico Circular")
plt.show()