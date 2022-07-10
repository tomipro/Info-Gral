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


def bubbleSort2(arr: List):
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


def mesGeneracion(lsArch: List, cant: int):
    lsArch = lsArch[1:]
    lstDatos = list()
    lstGen = list()
    lstFecha = list()

    for i in lsArch:
        dato = i.split(",")
        dato[4] = int(dato[4])
        lstDatos.append(dato)

    for j in lstDatos:
        lstGen.append(j[4])
        lstFecha.append(j[5])

    bubbleSort(lstGen)
    lstGen = lstGen[:cant]

    lista1 = list()
    lista2 = list()
    for k in lstDatos:
        for l in lstGen:
            if k[4] == l:
                mes = k[5][5:7]
                generacion = k[4]
                tupla = (mes, generacion)
                lista1.append(mes)
                lista2.append(tupla)
                
    bubbleSort2(lista2)

    print("{:10}{:>10}".format("MES", "GENERACION"))
    for m in lista2:
        print("{:10}{:>10}".format(m[0], m[1]))

def main():
    lsArch = ['central,region,tecnologia,fuente_generacion,generacion_neta,anio_mes', 'CAPE,COMAHUE,TURBO GAS,Termica,21868984,2020-01\n', 'AESP,BUENOS AIRES,TURBO VAPOR,TERMICA,191938412,2021-01\n', 'ALSM,NOROESTE,PCTOR DIESEL, Termica,1002979,2017-03\n', 'ALICKI,COMAHUE,TURB HIDRAULICA,Hidraulica,100241172,2018-07\n', 'ARROHI,PATAGONICA,TURB HIDRAULICA, Hidráulica,11706,2015-08\n', 'ANAT,NOROESTE,MOTOR DIESEL, Termica, 7670154,2018-07\n',
              'APAR,BUENOS AIRES, TURBO VAPOR,Termica,1077474,2015-05\n', 'ARAUZO,NOROESTE,EOLICA,Renovable,844789,2017-01\n', 'AARCHI,COMAHUE,TURB HIDRAULICA,Hidraulica,2961,2021-01\n', 'ATUC,BUENOS AIRES,NUCLEAR,Nuclear,237063,2019-01\n', 'ULN1FV,CUYO,FOTOVOLTAICA,Renovable,5713062,2020-03\n', 'VSES,BUENOS AIRES,TURBO GAS,Termica,43969,2020-02\n', 'VLONEO,BUENOS AIRES,EOLICA,Renovable,1171871,2020-05\n']

    print("\nCASO PRUEBA 01 - cant = 5")
    mesGeneracion(lsArch, 5)

    print("\nCASO PRUEBA 02 - cant = 1")
    mesGeneracion(lsArch, 1)

    print("\nCASO PRUEBA 03 - cant = 100")
    mesGeneracion(lsArch, 100)

    print("\nCASO PRUEBA 04 - cant = 0")
    mesGeneracion(lsArch, 0)


main()
