"""Ejercicio 5.9

Lista de 10 aleatorios entre 1 y 50: cuenta pares e impares.
"""

from random import randint

l : list = [randint(1, 50) for _ in range(10)]

pares : int = sum(1 for n in l if n % 2 == 0)
impares : int = len(l) - pares

print(l)
print("pares:", pares, "impares:", impares)
