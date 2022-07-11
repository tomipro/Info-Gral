from typing import List


def bubbleSort(arr: List):
    n = len(arr)
    for i in range(0, n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swapped = True

        if not swapped:
            return


def maximo(lsArch: List, n: int):
    lstTitulo = titulo(lsArch)
    lstDatos = datos(lsArch)
    lstFecha = list()
    lstGen = list()

    for i in lstDatos:
        lstFecha.append(i[4])
        lstGen.append(i[3])
    
    bubbleSort(lstGen)

    lstGen = lstGen[:n]

    lista1 = list()
    lista2 = list()

    for j in lstDatos:
        for k in lstGen:
            if j[3] == k:
                central = j[0]
                generacion = j[3]
                fecha = j[4]
                tupla = (central, generacion, fecha)
                lista1.append(fecha)
                lista2.append(tupla)

    bubbleSort(lista1)

    print("{:10}{:^10}{:>10}".format(lstTitulo[0], lstTitulo[1], lstTitulo[2]))
    for m in lista1:
        for n in lista2:
            if m == n[2]:
                print("{:10}{:^10}{:>10}".format(n[0], n[1], n[2]))


def datos(lsArch: List) -> List:
    lsArch = lsArch[1:]
    lst = list()

    for i in lsArch:
        i = i[:-1]
        dato = i.split(",")
        dato[3] = int(dato[3])
        lst.append(dato)
    
    return lst

def titulo(lsArch: List):
    lsArch = lsArch[:1]
    lstTitulo = list()

    for i in lsArch:
        i = i[:-1]
        i = i.split(",")

    lstTitulo.append(i[0])
    lstTitulo.append(i[3])
    lstTitulo.append(i[4])

    return lstTitulo


def main():
    lsArch = ['central,region,fuente,generacion,anio_mes\n', 'CAPE,COMAHUE,Termica,21868984,2020-01\n', 'AESP,BUENOS AIRES,Termica,193938412,2012-01\n', 'CAPE,COMAHUE,Termica,20009911,2017-03\n', 'ATUC,BUENOS AIRES,Nuclear,269321,2020-03\n', 'AMEGHI,PATAGONICA,Hidraulica,11705,2018-08\n', 'ANAT,NOROESTE,Termica,7670154,2018-07\n',
              'APAR,BUENOS AIRES,Termica,1077474,2015-09\n', 'ARAUEO,NOROESTE,Renovable,844759,2017-02\n', 'ARROHI,COMAHUE,Hidraulica,2961,2012-01\n', 'ATUC,BUENOS AIRES,Nuclear,237003,2019-03\n', 'ULN1FV,CUYO,Renovable,5779081,2020-03\n', 'APAR,BUENOS AIRES,Termica,43969,2020-02\n', 'VLONEO,BUENOS AIRES,Renovable,1171872,2020-02\n']
    n = int(input())
    print("Para n =", n)
    maximo(lsArch, n)


main()
