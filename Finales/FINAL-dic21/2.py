from typing import Dict, List


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


def filtrar(lsArch: List, lsCol: List, diFiltro: Dict):
    pass


def main():
    lsArch = ['central,region,fuente,generacion,anio_mes\n', 'CAPE,COMAHUE,Termica,21868984,2020-01\n', 'AESP,BUENOS AIRES,Termica,193938412,2012-01\n', 'CAPE,COMAHUE,Termica,20009911,2017-03\n', 'ATUC,BUENOS AIRES,Nuclear,269321,2020-03\n', 'AMEGHI,PATAGONICA,Hidraulica,11705,2018-08\n', 'ANAT,NOROESTE,Termica,7670154,2018-07\n',
              'APAR,BUENOS AIRES,Termica,1077474,2015-09\n', 'ARAUEO,NOROESTE,Renovable,844759,2017-02\n', 'ARROHI,COMAHUE,Hidraulica,2961,2012-01\n', 'ATUC,BUENOS AIRES,Nuclear,237003,2019-03\n', 'ULN1FV,CUYO,Renovable,5779081,2020-03\n', 'APAR,BUENOS AIRES,Termica,43969,2020-02\n', 'VLONEO,BUENOS AIRES,Renovable,1171872,2020-02\n']
    lsCol = ['central', 'anio_mes']
    diFiltro = {'anio_mes': '2020-01'}
    filtrar(lsArch, lsCol, diFiltro)


main()
