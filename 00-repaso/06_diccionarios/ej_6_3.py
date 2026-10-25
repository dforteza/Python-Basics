"""Ejercicio 6.3

Añade la clave 'profesion' a un diccionario existente.
"""

persona : dict = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

persona["profesion"] = "Sysadmin"   # si la clave ya existe, la sobrescribe
print(persona)
