
import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
porcentajepersonas = ["cabello corto", "cabello largo", "calvos"]
tamaños = [40, 35, 25]

# Crear gráfico circular
plt.pie(tamaños, labels=porcentajepersonas, autopct="%1.1f%%", startangle=140)
plt.title("Gráfico Circular")
plt.show()

import matplotlib.pyplot as plt

# Datos de ejemplo
x = [5, 7, 8, 7, 2, 17, 2, 9]
y = [99, 86, 87, 88, 100, 86, 103, 87]

# Crear gráfico de dispersión
plt.scatter(x, y, color="purple")
plt.title("Gráfico de Dispersión")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()


import matplotlib.pyplot as plt

# Datos de ejemplo
categorias = ["Cabello corto", "Cabello largo", "Calvos"]
tamaños = [40, 35, 25]

# Crear gráfico circular
plt.pie(tamaños, labels=categorias, autopct="%1.1f%%", startangle=140)
plt.title("Gráfico Circular")
plt.show()


