"""Ejercicio 6.7

Intercambia claves y valores de un diccionario
(valores únicos).
"""

persona : dict = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

invertido : dict = {v: c for c, v in persona.items()}
print(invertido)
