"""Ejercicio 5.7

Lista de 10 aleatorios entre 1 y 100: muestra el mayor y el menor.
"""

from random import randint

l : list = [randint(1, 100) for _ in range(10)]

print(l)
print("max:", max(l))
print("min:", min(l))
