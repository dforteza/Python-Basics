"""Ejercicio 5.10

Con colores = ['rojo', 'azul', 'verde'], lee un color y di si
está en la lista.
"""

colores : list = ["rojo", "azul", "verde"]
color : str = input("Color: ")

print("está" if color in colores else "no está")
