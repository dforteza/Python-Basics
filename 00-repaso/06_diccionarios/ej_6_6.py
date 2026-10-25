"""Ejercicio 6.6

Une dict1 = {'a': ) o algo asi n, 'b': 2} y dict2 = {'b': 3, 'c': 4};
las claves repetidas suman sus valores.
"""

dict1 : dict = {"a": 1, "b": 2}
dict2 : dict = {"b": 3, "c": 4}

resultado : dict = dict1.copy()     # copia: así no modificamos dict1
for c, v in dict2.items():
    resultado[c] = resultado.get(c, 0) + v

print(resultado)
