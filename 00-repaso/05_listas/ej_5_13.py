"""Ejercicio 5.13

Dada una lista de números, elimina los impares y muéstrala.
Ojo: prueba con [1, 2, 3, 4, 5, 6, 6, 7, 10].
"""


numeros = [i for i in range(11)]

pares : list = [n for n in numeros if n % 2 == 0]
print(pares)
