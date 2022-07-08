from typing import List, Tuple


def bubbleSort(arr: List):
    n = len(arr)
    for i in range(0, n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j][1] > arr[j + 1][1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swapped = True

        if not swapped:
            return


def minimos(lstEnergia: List) -> List[Tuple]:
    energia = list()
    for i in lstEnergia:
        dato = i.split(",")
        dato[1] = int(dato[1])  # idParque
        dato[2] = float(dato[2])  # cantidadEnergia
        energia.append(dato)

    aaEnergia = list()
    aaMmEnergia = list()
    for j in energia:
        anio = j[0][:2]
        anioMes = j[0][:4]
        # idParque = j[1]
        cantEnergia = j[2]
        aaEnergia.append([anio, cantEnergia])
        aaMmEnergia.append([anioMes, cantEnergia])
    
    bubbleSort(aaEnergia)
    bubbleSort(aaMmEnergia)

    resAnio = aaEnergia[0][0]
    resEnergiaAnio = aaEnergia[0][1]
    resAnioMes = aaMmEnergia[0][0]
    resEnergiaAnioMes = aaMmEnergia[0][1]

    return [(resAnio, resEnergiaAnio), (resAnioMes, resEnergiaAnioMes)]


def main():
    print("Prueba para el EJ01")
    lstEnergia = ['101205,1,24.2\n', '110607,8,54.4\n', '120318,3,18.1\n',
                  '090501,9,88.4\n', '101209,1,26.8\n', '101217,3,22.4\n', '190101,8,44.0\n']
    print(minimos(lstEnergia))


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

Prueba para el EJ01:

[('12', 18.1), ('1203', 18.1)]

'''
