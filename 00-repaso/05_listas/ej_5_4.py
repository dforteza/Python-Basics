"""Ejercicio 5.4

Guarda el abecedario en una lista, elimina las letras en
posiciones múltiplo de 3 y muestra el resultado.
"""

a = "abcdefghijklmnopqrstuvwxyz"
l : list = [letra for i, letra in enumerate(a, start=1) if (i % 3 != 0)]

print(l)