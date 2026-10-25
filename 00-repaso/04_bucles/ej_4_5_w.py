"""Ejercicio 4.5.w

Genera un aleatorio entre 1 y 100 (random.randint) y pide
números hasta acertarlo, dando pistas de mayor/menor.
"""
from random import randint

n = randint(1, 100)
print("Numero random", n)

while (True):
    m = int(input("numero: "))
    if m > n:
        print("mayor")
    elif m < n:
        print("menor")
    else:
        print("eureka")
        break