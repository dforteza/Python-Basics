"""Ejercicio 2.6

Pide una fecha dd/mm/aaaa y muestra día, mes y año por separado.
Debe funcionar también si día o mes tienen un solo dígito.
"""

f : str = "24/12/2002"
new_f = f.split("/", 2)

for c in new_f:
    print(c)
