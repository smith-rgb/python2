import matplotlib.pyplot as plt

# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Crear gráfico de líneas
plt.plot(x, y, marker="o", color="green", linestyle="--")
plt.title("Gráfico de Líneas")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()