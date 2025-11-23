import matplotlib.pyplot as plt

versiones = ["Original", "Optimizado"]
tiempos = [46.2079, 0.001]  # tus tiempos reales

plt.bar(versiones, tiempos)
plt.title("Comparación de tiempos de ejecución")
plt.xlabel("Versión del código")
plt.ylabel("Tiempo (segundos)")

plt.savefig("comparacion_tiempos.png")  # guarda la imagen
plt.show()
