

# criaro gerador de numeros aleatorios
import random

# criar lista de numeros
numeros = []

# criar lista de numeros
for i in range(10):
    # adicionar numeros aleatorios a lista
    numeros.append(random.randint(1, 100))

# criar lista de numeros
numeros.sort()

# criar lista de numeros
print("Lista de numeros aleatorios: ", numeros)
