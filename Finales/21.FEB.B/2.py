from typing import List


def bubbleSort(arr: List):
    n = len(arr)
    for i in range(0, n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j][1] < arr[j + 1][1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swapped = True

        if not swapped:
            return


def energiaTotal(n: int, lstEnergia: List, lstParque: List) -> List[List]:
    todo = list()

    energia = list()
    for i in lstEnergia:
        dato = i.split(",")
        dato[1] = int(dato[1])  # idParque
        dato[2] = float(dato[2])  # energia
        energia.append(dato)

    parque = list()
    for j in lstParque:
        dato = j.split(",")
        dato[0] = int(dato[0])  # idParque
        dato[2] = int(dato[2])  # cantMolinos
        parque.append(dato)

    lst = list()
    for k in parque:
        idParque = k[0]
        nombre = k[1]
        cantMolinos = k[2]
        enerTot = float()
        for e in energia:
            if idParque == e[1]:
                enerTot += e[2]
        lst.append([nombre, enerTot, enerTot / cantMolinos])

    bubbleSort(lst)

    lstFinal = list()
    for x in range(0, n):
        lstFinal.append(lst[x])

    return lstFinal


def main():
    print("Prueba para el EJ02")
    lstEnergia = ['101205,1,24.2\n', '110607,8,54.4\n', '120318,3,18.1\n',
                  '090501,9,88.4\n', '101209,1,26.8\n', '101217,3,22.4\n', '190101,8,44.0\n']
    lstParque = ['1,Rosario,8\n', '6,San Martin,4\n', '8,Lavalle,10\n',
                 '3,Esperanza,3\n', '7,General Pico,9\n', '9,P.Madryn,4\n']
    print(energiaTotal(3, lstEnergia, lstParque))


main()

'''
Desarrollar la función energiaTotal(n, lstEnergia, lstParque), que recibe por parámetro un
valor entero n (que representa una cantidad) y las dos listas con los datos. A partir de la información que contiene
lstEnergia y lstParque, determinar:

    ● Los n parques eólicos que MAYOR Cantidad de Energía total es producida por el Parque (CEP). (nota1).
    Y para cada uno de estos en parques, determinar (CEM): la Cantidad de Energía que produce cada
    Molino de un parque determinado (nota2).
        
        a. (nota1).: (CEP) se obtiene de sumar toda la energía producida de cada día, para un determinado
        parque.
        b. (nota2).: (CEM) Se obtiene de dividir la cantidad total de energía que produce un parque dividido la
        cantidad de molino que tiene dicho parque.

La función deberá retornar una lista de lista de n elementos donde cada elemento de la sublista contiene el
nombre del parque, el CEP y el CEM para dicho parque.

Estructura de cada elemento de la sublista a retornar ->
    [ nombre_parque, CEP , CEM ]

Prueba para el EJ02:

[['Lavalle', 98.4, 9.84], ['P.Madryn', 88.4, 22.1], ['Rosario', 51.0, 6.375]]

'''
