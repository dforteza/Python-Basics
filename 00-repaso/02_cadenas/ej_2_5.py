"""Ejercicio 2.5

Pide una frase y una vocal; muestra la frase con esa vocal
en mayúscula.
"""

f : str = input("Frase: ")
v : str = input("Vocal: ")

new : str = f.replace(v, v.upper())
print(new)        