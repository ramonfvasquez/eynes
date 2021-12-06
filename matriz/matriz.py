"""Crear una matriz de 5x5 randomizada con números enteros, encontrar secuencia de 4
números consecutivos horizontal o vertical y si se encuentra mostrar la posición inicial y
final.

Ejemplos:

MATRIZ 1: 
>>> matriz1 = [
...    [1, 2, 3, 4, 5],
...    [2, 3, 4, 5, 6],
...    [3, 4, 5, 6, 7],
...    [4, 5, 6, 7, 8],
...    [5, 6, 7, 8, 9]
... ]
>>> consecutivos_por_fila(matriz1)
[{'fila': [1, 2, 3, 4, 5], 'inicial': (1, 1), 'final': (1, 4)}, {'fila': [2, 3, 4, 5, 6], 'inicial': (2, 1), 'final': (2, 4)}, {'fila': [3, 4, 5, 6, 7], 'inicial': (3, 1), 'final': (3, 4)}, {'fila': [4, 5, 6, 7, 8], 'inicial': (4, 1), 'final': (4, 4)}, {'fila': [5, 6, 7, 8, 9], 'inicial': (5, 1), 'final': (5, 4)}]

>>> consecutivos_por_columna(matriz1)
[{'col': [1, 2, 3, 4, 5], 'inicial': (1, 1), 'final': (4, 1)}, {'col': [2, 3, 4, 5, 6], 'inicial': (1, 2), 'final': (4, 2)}, {'col': [3, 4, 5, 6, 7], 'inicial': (1, 3), 'final': (4, 3)}, {'col': [4, 5, 6, 7, 8], 'inicial': (1, 4), 'final': (4, 4)}, {'col': [5, 6, 7, 8, 9], 'inicial': (1, 5), 'final': (4, 5)}]


MATRIZ 2:
>>> matriz2 = [
...    [1, 2, 2, 4, 5],
...    [2, 3, 4, 5, 6],
...    [4, 4, 5, 1, 1],
...    [4, 3, 6, 7, 8],
...    [5, 6, 7, 8, 1]
... ]

>>> consecutivos_por_fila(matriz2)
[{'fila': [2, 3, 4, 5, 6], 'inicial': (2, 1), 'final': (2, 4)}, {'fila': [5, 6, 7, 8, 1], 'inicial': (5, 1), 'final': (5, 4)}]

>>> consecutivos_por_columna(matriz2)
[{'col': [2, 4, 5, 6, 7], 'inicial': (2, 3), 'final': (5, 3)}]


MATRIZ 3:
>>> matriz3 = [
...    [3, 2, 2, 4, 5],
...    [2, 1, 4, 5, 6],
...    [4, 4, 5, 1, 1],
...    [4, 3, 4, 7, 8],
...    [5, 5, 5, 8, 9]
... ]

>>> consecutivos_por_fila(matriz3)
[]

>>> consecutivos_por_columna(matriz3)
[]


MATRIZ 4:
>>> matriz4 = [
...    [3, 2, 2, 4, 5],
...    [2, 1, 4, 5, 6],
...    [2, 3, 4, 5, 1],
...    [4, 3, 4, 7, 8],
...    [5, 5, 5, 8, 9]
... ]

>>> consecutivos_por_fila(matriz4)
[{'fila': [2, 3, 4, 5, 1], 'inicial': (3, 1), 'final': (3, 4)}]

>>> consecutivos_por_columna(matriz4)
[]


MATRIZ 5:
>>> matriz5 = [
...    [3, 2, 4, 4, 5],
...    [2, 1, 3, 5, 6],
...    [1, 3, 4, 5, 1],
...    [4, 3, 5, 7, 8],
...    [5, 5, 6, 8, 9]
... ]

>>> consecutivos_por_fila(matriz5)
[]

>>> consecutivos_por_columna(matriz5)
[{'col': [4, 3, 4, 5, 6], 'inicial': (2, 3), 'final': (5, 3)}]
"""

import doctest
import random as R


def crear_matriz(filas=5, cols=5, min=1, max=4):
    return [[R.randint(min, max) for _ in range(cols)] for _ in range(filas)]


def consecutivos_por_fila(matriz):
    consecutivos = []

    # Recorre la matriz fila por fila
    for f_index, fila in enumerate(matriz):
        contador = 0
        inicial = None
        final = None

        # Recorre cada elemento de la fila excepto el último
        for i in range(len(fila) - 1):
            # Si el elemento + 1 es igual al elemento siguiente,
            # entonces son consecutivos y suma al contador.
            # Cuando el contador vale 1, asigna una tupla con las
            # coordenadas a inicial; cuando vale 3, le asigna una
            # tupla con coordenadas a final. A los valores de las
            # filas y las columnas se les suma 1 para que los números
            # no empiecen en 0 (el primer elemento de la matriz
            # será [1, 1]).
            # A la segunda coordenada de final se le suma 2
            # porque cuando el contador vale 3, el elemento
            # seleccionado en el loop es el tercero, no el cuarto;
            # de esta manera, al sumarle 2 a la columna final, se
            # están marcando las coordenadas del cuarto elemento
            # de la sucesión. Las coordenadas finales solo indican
            # la posición del cuarto elemento, independientemente
            # de si la sucesión tiene más elementos.
            if fila[i] + 1 == fila[i + 1]:
                contador += 1

                if contador == 1:
                    inicial = (f_index + 1, i + 1)
                elif contador == 3:
                    final = (f_index + 1, i + 2)
                    consecutivos.append(
                        {"fila": fila, "inicial": inicial, "final": final}
                    )
                    continue
            else:
                contador = 0

    return consecutivos


def consecutivos_por_columna(matriz):
    consecutivos = []

    # Recorre cada elemento de la fila excepto el último
    for i in range(len(matriz)):
        contador = 0
        inicial = 0
        final = 0
        col = []

        for j in range(len([fila for fila in matriz])):
            # Si el elemento + 1 es igual al elemento siguiente,
            # entonces son consecutivos y suma al contador.
            # Cuando el contador vale 1, asigna una tupla con las
            # coordenadas a inicial; cuando vale 3, le asigna una
            # tupla con coordenadas a final. A los valores de las
            # filas y las columnas se les suma 1 para que los números
            # no empiecen en 0 (el primer elemento de la matriz
            # será [1, 1]).
            # A la primera coordenada de final se le suma 2
            # porque cuando el contador vale 3, el elemento
            # seleccionado en el loop es el tercero, no el cuarto;
            # de esta manera, al sumarle 2 a la fila final, se
            # están marcando las coordenadas del cuarto elemento
            # de la sucesión. Las coordenadas finales solo indican
            # la posición del cuarto elemento, independientemente
            # de si la sucesión tiene más elementos.
            if j < len(matriz) - 1:
                if matriz[j][i] + 1 == matriz[j + 1][i]:
                    contador += 1

                    if contador == 1:
                        inicial = (j + 1, i + 1)
                    if contador == 3:
                        final = (j + 2, i + 1)
                else:
                    contador = 0

            col.append(matriz[j][i])

        if contador >= 3:
            consecutivos.append({"col": col, "inicial": inicial, "final": final})

    return consecutivos


def main():
    matriz = crear_matriz()

    print("MATRIZ:")
    for fila in matriz:
        print(fila)

    print()

    print("CONSECUTIVOS POR FILA:")
    print(consecutivos_por_fila(matriz))

    print()

    print("CONSECUTIVOS POR COLUMNA:")
    print(consecutivos_por_columna(matriz))


if __name__ == "__main__":
    main()
    doctest.testmod()
