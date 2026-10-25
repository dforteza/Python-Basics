"""Ejercicio 5.3

Pide 5 números, guárdalos en una lista y muéstralos ordenados
de menor a mayor.
"""

l : list = []
for _ in range(5):
    l.append(int(input("Número: ")))

l.sort()            # ordena en el sitio y devuelve None
print(l)
print(sorted(l))    # devuelve una lista nueva
