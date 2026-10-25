"""Ejercicio 4.8

Pide un número y muéstralo invertido (sin convertirlo a str).
"""

n = 321
res = 0
while (n != 0):
    res = 10 * res + (n % 10)
    n //= 10

print(res)