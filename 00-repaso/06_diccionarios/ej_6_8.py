"""Ejercicio 6.8

Pide nombres de estudiantes y sus notas, guárdalos en un
diccionario y muestra la nota más alta.
"""

notas : dict = {}
while True:
    nombre = input("Estudiante (fin para acabar): ")
    if nombre == "fin":
        break
    notas[nombre] = int(input("Nota: "))

print(max(notas))                       # la clave mayor (alfabética), no la nota
print(max(notas.values()))              # la nota más alta
mejor = max(notas, key=lambda n: notas[n])
print(mejor, notas[mejor])              # quién la tiene
