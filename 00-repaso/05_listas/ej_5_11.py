"""Ejercicio 5.11

Genera la lista de primos del 1 al 100.
"""


def es_primo(n: int) -> bool:
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


primos : list = [n for n in range(1, 101) if es_primo(n)]
print(primos)
