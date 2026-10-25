"""Ejercicio 6.2

Con {'nombre': 'Ana', 'edad': 25, 'ciudad': 'Madrid'},
imprime el valor de 'edad'.
"""

persona : dict = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

print(persona["edad"])          # KeyError si la clave no existe
print(persona.get("altura"))    # None si la clave no existe
