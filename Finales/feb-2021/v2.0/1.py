from typing import List, Tuple


def minimos(lstEnergia: List) -> Tuple:
    pass


def main():
    print("Prueba para el EJ01")
    lstEnergia = ['101205,1,24.2\n', '110607,8,54.4\n', '120318,3,18.1\n',
                  '090501,9,88.4\n', '101209,1,26.8\n', '101217,3,22.4\n', '190101,8,44.0\n']
    (minimos(lstEnergia))


main()


'''
Desarrollar la función minimos(lstEnergia) que a partir de la información que contiene lstEnergia la
función deberá determinar:
    ● El año “AA” donde se produce la menor energía, y la cantidad de energía generada “cEnergiaA” en
    dicho año.
    ● El mes (con el año) “AAMM” donde se produce la menor energía, y la cantidad de energía generada
    “cEnergiaM” para dicho mes / Año.

La función deberá retornar una lista conteniendo dos tuplas, donde cada tupla contiene los valores
determinadas anteriormente, cómo se muestra a continuación:
    Formato de la lista a retornar -> [(AA,cEnergiaA), (AAMM,cEnergiaM)]

Prueba para el EJ01

[('12', 18.1), ('1203', 18.1)]

'''
