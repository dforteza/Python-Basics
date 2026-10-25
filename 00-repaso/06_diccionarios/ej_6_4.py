"""Ejercicio 6.4

Borra la clave 'ciudad' de un diccionario y muestra el resultado.
"""

persona : dict = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

del persona["ciudad"]               # o persona.pop("ciudad"), que devuelve el valor
print(persona)
