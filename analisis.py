import pandas as pd 


# # Crear una Serie
# serie = pd.Series([1, 2, 3, 4, 5])

# # Crear un DataFrame
# datos = {"Nombre": ["Ana", "Juan", "Pedro"], "Edad": [25, 30, 35]}
## Leer un archivo CSV
df = pd.read_csv("poblacion.csv")

print(df)
# Escribir en un archivo CSV
df.to_csv("poblacion.csv", index=False)

# df.head(5)       # Primeras 5 filas
# df.tail(5)       # Últimas 5 filas
# df.info(5)       # Información general
# df.describe(5)   # Estadísticas descriptivas

print(df["COL"])

print(df[df["Date"]>2020])

# df["nuevopais"]= df["COL"] + 1000000
print(df)


print(df["ARG"].mean())
