"""Ejercicio 6.5.f

Con for, imprime claves y valores de un diccionario.
"""

persona : dict = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

for clave, valor in persona.items():
    print(f"{clave}: {valor}")
