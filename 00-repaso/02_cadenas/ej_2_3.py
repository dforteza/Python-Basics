"""Ejercicio 2.3

Pide un teléfono con formato prefijo-número-extensión
(ej. +34-913724710-56) y muestra solo el número.
"""
tlf : str = "+34-913724710-56"
a = tlf.split('-', 2)
if len(a) != 3:
    exit()

print(a[1])