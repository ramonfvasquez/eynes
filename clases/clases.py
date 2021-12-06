"""Escribir una clase en python llamada círculo que contenga un radio, con un método que
devuelva el área y otro que devuelva el perímetro del círculo.

Si se instancia la clase con radio <= 0 mostrar una excepción indicando un error amigable al
usuario e impidiendo la instanciación.

Si printeamos el objeto creado debe mostrarse una representación amigable.

El objeto debe tener su atributo radio modificable, si se le intenta setear un valor <= 0
mostrar un error y no permitir modificación.

Permitir la multiplicación del circulo: Circulo * n debe devolver un nuevo objeto con el radio
multiplicado por n. No permitir la multiplicación por números <= 0.

Ejemplos:

CÍRCULO 1:
>>> circulo1 = Circulo(radio=3)
>>> print(circulo1)
El círculo de radio 3 tiene un área de 28.2744 y un perímetro de 18.8496.


CÍRCULO 2:
>>> circulo1 = Circulo(radio=3)
>>> circulo2 = circulo1 * 3
>>> print(circulo2)
El círculo de radio 9 tiene un área de 254.46959999999999 y un perímetro de 56.5488.


CÍRCULO 3:
>>> circulo1 = Circulo(radio=3)
>>> circulo2 = circulo1 * (-2)
Traceback (most recent call last):
ValueError: No se puede multiplicar por valores iguales o menores a 0.


CÍRCULO 4:
>>> circulo = Circulo(radio=-2)
Traceback (most recent call last):
ValueError: No se puede crear un círculo de radio igual o menor a 0.
"""

import doctest

PI = 3.1416


class Circulo:
    def __init__(self, radio=1):
        # Si se intenta instanciar un círculo con un radio igual o menor a 0,
        # se eleva un ValueError y la instanciación se impide.
        if radio <= 0:
            raise ValueError("No se puede crear un círculo de radio igual o menor a 0.")
        else:
            self._radio = radio

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, rad):
        # Si se intenta cambiar el radio por un valor igual o menor a 0, eleva un
        # ValueError e impide que se cambie el valor del radio.
        if rad <= 0:
            raise ValueError("El radio no puede ser igual o menor a 0.")
        else:
            self._radio = rad

    def area(self):
        return PI * self.radio ** 2

    def perimetro(self):
        return 2 * PI * self.radio

    def __str__(self):
        # Al hacer un print del objeto círculo, muestra un mensaje con el radio,
        # el área y el perímetro del objeto.
        return (
            f"El círculo de radio {self.radio} tiene un área de {self.area()} "
            + f"y un perímetro de {self.perimetro()}."
        )

    def __mul__(self, otro):
        # Al multiplicar un objeto círculo por un número n, crea un nuevo objeto
        # círculo con un radio igual al radio del círculo original multiplicado
        # por n.
        # Si se intenta multiplicar por un valor menor o igual a 0 (lo que daría
        # un valor de radio erróneo), eleva un ValueError, muestra un mensaje e
        # impide la creación del nuevo objeto.
        if otro > 0:
            return Circulo(radio=self.radio * otro)
        else:
            raise ValueError(
                "No se puede multiplicar por valores iguales o menores a 0."
            )

    __rmul__ = __mul__


if __name__ == "__main__":
    doctest.testmod()
