from typing import Dict, List, NoReturn


def filtrar(lstArch: List, lstCol: List, diFiltro: Dict) -> NoReturn:

    lstTot = []
    for i in lstArch:
        a = i[:-1]
        lstA = a.split(",")
        lstTot.append(lstA)

    filtro = -1
    aux = -1
    for i in lstTot[0]:
        aux += 1
        if i in diFiltro.keys():
            filtro = aux

    lstFiltrada = []

    if filtro != -1:
        lstFiltrada.append(lstTot[0])
        for i in lstTot:
            if i[filtro] in diFiltro.values():
                lstFiltrada.append(i)
    elif filtro == -1:
        lstFiltrada += lstTot

    for i in range(len(lstFiltrada)):
        for j in range(len(lstFiltrada[0])):
            if lstFiltrada[0][j] in lstCol:
                print("{:<15}".format(lstFiltrada[i][j]), end=" ")
        print(" ")


def main():
    lstArch = ['central,region,fuente,generacion,anio_mes\n', 'CAPE,COMAHUE,Termica,21868984,2020-01\n', 'AESP,BUENOS AIRES,Termica,193938412,2012-01\n', 'CAPE,COMAHUE,Termica,20009911,2017-03\n', 'ATUC,BUENOS AIRES,Nuclear,269321,2020-03\n', 'AMEGHI,PATAGONICA,Hidraulica,11705,2018-08\n', 'ANAT,NOROESTE,Termica,7670154,2018-07\n',
               'APAR,BUENOS AIRES,Termica,1077474,2015-09\n', 'ARAUEO,NOROESTE,Renovable,844759,2017-02\n', 'ARROHI,COMAHUE,Hidraulica,2961,2012-01\n', 'ATUC,BUENOS AIRES,Nuclear,237003,2019-03\n', 'ULN1FV,CUYO,Renovable,5779081,2020-03\n', 'APAR,BUENOS AIRES,Termica,43969,2020-02\n', 'VLONEO,BUENOS AIRES,Renovable,1171872,2020-02\n']
    lstCol = ['central', 'fuente', 'anio_mes']
    diFiltro = {}
    filtrar(lstArch, lstCol, diFiltro)


main()
