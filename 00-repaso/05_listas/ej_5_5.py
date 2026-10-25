"""Ejercicio 5.5

Pide una palabra y muestra cuántas veces aparece cada vocal.
"""

s : str = input("Palabra: ").lower()

for v in "aeiou":
    print(v, s.count(v))
