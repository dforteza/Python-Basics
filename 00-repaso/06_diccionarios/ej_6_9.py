"""Ejercicio 6.9

Diccionario de personas -> {edad, ciudad}. Permite consultar
por consola un dato de una persona.
"""

personas : dict = {
    "ana": {"edad": 29, "ciudad": "Madrid"},
    "luis": {"edad": 19, "ciudad": "Bilbao"},
}

nombre : str = input("Persona: ")
info = personas.get(nombre)             # None si no existe
if info is None:
    print("No conozco a esa persona")
else:
    dato : str = input("Dato (edad/ciudad): ")
    print(info.get(dato, "Dato no disponible"))
