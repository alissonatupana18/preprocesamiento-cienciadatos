import numpy as np
import time
from math import sqrt

def es_primo_np(n):
    if n <= 1:
        return False
    return not np.any(n % np.arange(2, int(sqrt(n)) + 1) == 0)

inicio = time.time()

primos = [i for i in range(1, 100000) if es_primo_np(i)]

fin = time.time()
print("Tiempo optimizado:", fin - inicio, "segundos")
