"""Ejercicio 5.8

Lista de 10 aleatorios entre 1 y 100: ordénalos de mayor a menor.
"""

from random import randint

l : list = [randint(1, 100) for _ in range(10)]

l.sort(reverse=True)
print(l)
