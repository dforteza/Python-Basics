"""Ejercicio 2.1

Pide un nombre por consola y muéstralo: tal cual, en minúsculas,
en mayúsculas y con la primera letra de cada palabra en mayúscula.
"""

nombre : str = input("nombre: ")
print("mayusc:", nombre.upper())
print("mayusc:", nombre.lower())
print("mayusc:", nombre.title())

