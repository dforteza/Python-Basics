"""Ejercicio 5.12

Dadas dos listas, muestra los elementos en común.
"""

l1 : list = [1, 2, 3, 4, 5]
l2 : list = [2, 4, 6]

# con un bucle: "in" ya recorre l2 por dentro
comunes : list = [x for x in l1 if x in l2]
print(comunes)

# con conjuntos: & es la intersección
print(set(l1) & set(l2))
