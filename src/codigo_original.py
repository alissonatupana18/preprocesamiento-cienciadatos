import time

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

inicio = time.time()

primos = []
for i in range(1, 100000):
    if es_primo(i):
        primos.append(i)

fin = time.time()
print("Tiempo de ejecución:", fin - inicio, "segundos")
