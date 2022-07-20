from typing import List, Tuple


def bubbleSort(lst: List):
    n = len(lst)
    for i in range(0, n):
        swapped = False
        for j in range(0, n - i - 1):
            if lst[j][1] < lst[j + 1][1]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp
                swapped = True

        if not swapped:
            return


def media_01(n: int, lstCiudad: List, lstResiduos: List) -> Tuple:
    ciudad = list()
    for i in lstCiudad:
        dato = i.split(",")
        dato[0] = int(dato[0])
        dato[1] = dato[1][:-1]
        ciudad.append(dato)

    res = list()
    for j in lstResiduos:
        dato = j.split(",")
        dato[0] = int(dato[0])
        dato[1] = int(dato[1])
        dato[2] = int(dato[2])
        res.append(dato)

    lst = list()
    resTot = int()
    cantCiudades = int()
    for k in ciudad:
        idCiudad = k[0]
        nomCiudad = k[1]
        residuos = int()
        fecha = int()
        for l in res:
            if l[1] == idCiudad:
                cantCiudades += 1
                residuos += l[0]
                fecha += 1
        resTot += residuos
        promedio = residuos / fecha
        lst.append([nomCiudad, round(promedio, 1)])
    promTotal = round((resTot / cantCiudades), 2)
    bubbleSort(lst)
    lstFinal = list()
    for x in lst:
        if len(lstFinal) < n:
            lstFinal.append(x)

    return (promTotal, lstFinal)


def main():
    print("Prueba para el EJ01")
    lstCiudad = ['223,Parana\n', '114,Merlo\n', '218,Guaymallen\n',
                 '132,C. Rivadavia\n', '341,Adolfo Alsina\n', '404,Jose C. Paz\n']
    lstResiduos = ['33,114,200518\n', '31,223,200519\n', '27,218,200319\n', '26,132,200616\n', '74,341,200319\n', '62,404,200606\n', '46,218,200709\n', '55,132,200630\n', '55,341,200612\n',
                   '54,404,200701\n', '23,114,200315\n', '55,223,200519\n', '34,218,200319\n', '33,132,200425\n', '27,341,200422\n', '21,404,200501\n', '31,114,200503\n', '44,114,200513\n', '44,218,200519\n']
    print(media_01(3, lstCiudad, lstResiduos))


main()


'''
Desarrollar la función media_01 (n,lstCiudad ,lstResiduos) que recibe por parámetro un número
entero n. y las listas lstCiudad y lstResiduos que contiene la información de lectura del archivo
correspondiente con readlines (cómo se indica arriba).

La función deberá calcular la media (promedio) de residuos para cada una de la ciudades y la media (promedio)
del total de residuo para todas las ciudades. La función deberá retornar una tupla de dos elementos
    ● En la posición 0(cero) de la tupla se debe encontrar un número “float” que representa la media (promedio)
    del total de residuo para todas las ciudades.
    ● En la posición 1(uno) de la tupla se debe encontrar una lista con sólo las n primeras ciudades que
    más residuos producen.
        ○ Cada elemento de dicha lista debe ser [ NombreCiudad , CantidadPormedioResiduo ]
            ■ NombreCiudad es un string
            ■ CantidadPormedioResiduo es un float

Prueba para el EJ01:
(40.78, [['Adolfo Alsina', 52.0], ['Jose C. Paz', 45.6], ['Parana', 43.0] ])
'''
