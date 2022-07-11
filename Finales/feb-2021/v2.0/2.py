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
    lstDatos = datos(lstEnergia, lstParque)
    energia = lstDatos[0]
    parques = lstDatos[1]

    lista = list()

    for i in parques:
        idParque = i[0]
        nombre = i[1]
        cantMolinos = i[2]
        energiaTot = float()
        for j in energia:
            if idParque == j[1]:
                energiaTot += j[2]
        lista.append([nombre, energiaTot, (energiaTot / cantMolinos)])

    bubbleSort(lista)

    return lista[:n]


def datos(lstEnergia: List, lstParque: List) -> List[List]:
    energia = list()
    parques = list()

    for i in lstEnergia:
        i = i[:-1]
        dato = i.split(",")
        dato[1] = int(dato[1])
        dato[2] = float(dato[2])
        energia.append(dato)

    for j in lstParque:
        j = j[:-1]
        dato = j.split(",")
        dato[0] = int(dato[0])
        dato[2] = int(dato[2])
        parques.append(dato)

    return [energia, parques]


def main():
    print("Prueba para el EJ02")
    lstEnergia = ['101205,1,24.2\n', '110607,8,54.4\n', '120318,3,18.1\n',
                  '090501,9,88.4\n', '101209,1,26.8\n', '101217,3,22.4\n', '190101,8,44.0\n']
    lstParque = ['1,Rosario,8\n', '6,San Martin,4\n', '8,Lavalle,10\n',
                 '3,Esperanza,3\n', '7,General Pico,9\n', '9,P.Madryn,4\n']
    print(energiaTotal(3, lstEnergia, lstParque))


main()


'''
EJ02

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

Estructura de cada elemento de la sublista a retornar -> [ nombre_parque, CEP , CEM ]

Prueba para el EJ02:

[['Lavalle', 98.4, 9.84], ['P.Madryn', 88.4, 22.1], ['Rosario', 51.0, 6.375]]
'''
