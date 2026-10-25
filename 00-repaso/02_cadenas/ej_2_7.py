"""Ejercicio 2.7

Pide los productos de una cesta separados por comas y muestra
cada producto en una línea.
"""

s : str = input("Compra: ")

new_s = s.split(", ")

print("\n".join(new_s))