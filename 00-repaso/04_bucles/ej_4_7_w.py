"""Ejercicio 4.7.w

Con while, pide un número y muestra la suma de sus dígitos
(591 -> 15).
"""

n = 591
sum = 0
while n != 0:
    sum += n % 10
    n //= 10

print(sum)