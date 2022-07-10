from typing import List


def bubbleSort(arr: List, col: int, ord: int):
    n = len(arr)

    if (ord != 0):
        for i in range(0, n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j][col] < arr[j + 1][col]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
                    swapped = True

        if not swapped:
            return

    else:
        for i in range(0, n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j][col] > arr[j + 1][col]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
                    swapped = True

            if not swapped:
                return


def archAlst(lsArch: List, col: int, ord: int) -> List[List]:
    lst = limpiarDatos(lsArch)

    datos = list()
    for i in lst:
        i[4] = int(i[4])
        i[5] = i[5][:-1]
        datos.append(i)

    if (col > 5):
        return datos

    else:
        bubbleSort(datos, col, ord)

    return datos


def limpiarDatos(lsArch: List):
    lsArch = lsArch[1:]
    lst = list()

    for i in lsArch:
        dato = i.split(",")
        lst.append(dato)

    return lst


def main():
    lsArch = ['central,region,tecnologia,fuente_generacion,generacion_neta,anio_mes\n', 'CAPE,COMAHUE,TURBO GAS,Termica,21668334,2020-01\n',
              'AESP,BUENOS AIRES,TURBO VAPOR,Termica,29333412,2017-01\n', 'ALEM,NOROESTE,MOTOR DIESEL,Termica,4032970,2017-03\n', 'ALICHI,COMAHUE,TURB HIDRAULICA,Hidraulica,100241172,2018-07\n']

    print("\nCASO PRUEBA 01 - col = 0, ord = 1")
    ls = archAlst(lsArch, col=0, ord=1)
    for sL in ls:
        print(sL)

    print("\nCASO PRUEBA 02 - col = 1, ord = 0")
    ls = archAlst(lsArch, col=1, ord=0)
    for sL in ls:
        print(sL)

    print("\nCASO PRUEBA 03 - col = 5, ord = 1")
    ls = archAlst(lsArch, col=5, ord=1)
    for sL in ls:
        print(sL)

    print("\nCASO PRUEBA 04 - col = 100, ord = 0")
    ls = archAlst(lsArch, col=100, ord=0)
    for sL in ls:
        print(sL)


main()
