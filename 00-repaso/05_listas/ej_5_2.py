"""Ejercicio 5.2

Lee valores por teclado hasta 'fin' y guárdalos en una lista.
"""

l : list = []
while True:
    v = input("Valor: ")
    if v == "fin":
        break
    l.append(v)

print(l)
