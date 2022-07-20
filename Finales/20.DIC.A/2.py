from typing import Dict, List


def bubbleSort(lst: List):
    n = len(lst)
    for i in range(0, n):
        swapped = False
        for j in range(0, n - i - 1):
            if lst[j] < lst[j + 1]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp
                swapped = True

        if not swapped:
            return


def media_02(lstResiduos: List) -> Dict:
    res = list()
    for i in lstResiduos:
        dato = i.split(",")
        dato[0] = int(dato[0])
        dato[1] = int(dato[1])
        dato[2] = (dato[2])
        res.append(dato)

    dic = dict()
    meses = list()
    for j in res:
        cantBasura = j[0]
        idCiudad = j[1]
        fecha = j[2]
        anio = int(j[2][4:-1])
        mes = int(j[2][2:4])

        if mes not in dic:
            residuos = int()
            cont = int()
            for k in res:
                if (mes == int(k[2][2:4])):
                    cont += 1
                    residuos += k[0]
            dic[mes] = residuos / cont
    return dic


def main():
    print("Prueba para el EJ02")
    lstResiduos = ['33,114,200518\n', '31,223,200519\n', '27,218,200319\n', '26,132,200616\n',
                   '74,341,200319\n', '62,404,200606\n', '46,218,200709\n', '55,132,200630\n', '55,341,200612\n',
                   '54,404,200701\n', '23,114,200315\n', '55,223,200519\n', '34,218,200319\n', '33,132,200425\n',
                   '27,341,200422\n', '21,404,200501\n', '31,114,200503\n', '44,114,200513\n', '44,218,200519\n']
    print(media_02(lstResiduos))


main()

'''

Desarrollar la función media_02(lstResiduos) que recibe por parámetro la lista lstResiduos que contiene
la información de lectura del archivo correspondiente con readlines (cómo se indica arriba).

La función deberá calcular la media (promedio) de residuos para cada mes (*) que figure en lstResiduos. y
retornar un diccionario con el promedio mensual de residuos generados. El diccionario debe cumplir la siguiente
especificación:

    ● Clave: debe ser un número entero que representa el número de mes. El rango válido es de 1 a 12
    inclusives.
    ● Valor: Es un número float que representa el promedio mensual.

(*) Importante: sólo DEBE contener las claves de aquellos meses que existan en lstResiduos. Si no se
encuentra el mes en dicha lista, no se deberá consignar la información en el diccionario. Además, debe considerar
para calcular la media como “mismo mes” a aquellas fechas que tengan el mes igual sin importar su año. Por
ejemplo, para el mes de Mayo, se debe calcular la media de todos los meses de Mayo que aparezcan en el
archivo, “sean del año que sean”.

Prueba para el EJ02:
{ 3: 39.5, 4: 30.0, 5: 37.0, 6: 49.5, 7: 50.0 }

'''
