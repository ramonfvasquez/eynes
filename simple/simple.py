"""Hacer una función que genere una lista de diccionarios que contengan id y edad,
donde edad sea un número aleatorio entre 1 y 100 y la longitud de la lista sea de 10
elementos. Retornar la lista.

Hacer otra función que reciba lo generado en la primer función y ordenarlo de mayor a
menor. Printear el id de la persona más joven y más vieja. Devolver la lista ordenada.

Ejemplos:

LISTA 1:
>>> ordenar_mayor_a_menor([
...    {'id': 0, 'edad': 12},
...    {'id': 1, 'edad': 45},
...    {'id': 2, 'edad': 44},
...    {'id': 3, 'edad': 57},
...    {'id': 4, 'edad': 69},
...    {'id': 5, 'edad': 32},
...    {'id': 6, 'edad': 23},
...    {'id': 7, 'edad': 12},
...    {'id': 8, 'edad': 81},
...    {'id': 9, 'edad': 72}
... ])
ID persona más joven: 0
ID persona más vieja: 8
[{'id': 8, 'edad': 81}, {'id': 9, 'edad': 72}, {'id': 4, 'edad': 69}, {'id': 3, 'edad': 57}, {'id': 1, 'edad': 45}, {'id': 2, 'edad': 44}, {'id': 5, 'edad': 32}, {'id': 6, 'edad': 23}, {'id': 7, 'edad': 12}, {'id': 0, 'edad': 12}]


LISTA 2:
>>> ordenar_mayor_a_menor([
...    {'id': 0, 'edad': 99},
...    {'id': 1, 'edad': 100},
...    {'id': 2, 'edad': 35},
...    {'id': 3, 'edad': 18},
...    {'id': 4, 'edad': 1},
...    {'id': 5, 'edad': 2},
...    {'id': 6, 'edad': 54},
...    {'id': 7, 'edad': 87},
...    {'id': 8, 'edad': 23},
...    {'id': 9, 'edad': 14}
... ])
ID persona más joven: 4
ID persona más vieja: 1
[{'id': 1, 'edad': 100}, {'id': 0, 'edad': 99}, {'id': 7, 'edad': 87}, {'id': 6, 'edad': 54}, {'id': 2, 'edad': 35}, {'id': 8, 'edad': 23}, {'id': 3, 'edad': 18}, {'id': 9, 'edad': 14}, {'id': 5, 'edad': 2}, {'id': 4, 'edad': 1}]
"""

import doctest
import random as R


def dict_list():
    return [{"id": i, "edad": R.randint(1, 100)} for i in range(10)]


def ordenar_mayor_a_menor(lista):
    ordenada = sorted(lista, key=lambda item: (item["edad"], item["id"]), reverse=True)

    print("ID persona más joven:", ordenada[-1]["id"])
    print("ID persona más vieja:", ordenada[0]["id"])

    return ordenada


if __name__ == "__main__":
    doctest.testmod()
