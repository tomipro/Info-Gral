from typing import List


def lsDominio(lsArch: List, lsCol: List, lsRes: List):
    lstTitulo = titulo(lsArch)
    lsArch = lsArch[1:]
    lst = datos(lsArch)
    # print(lst)
    print(lstTitulo)
    lstFinal = list()
    i = 0
    lstInd = list()

    if ('central' in lsCol):
        lstInd.append(0)
    
    if ('region' in lsCol):
        lstInd.append(1)
    
    if ('fuente' in lsCol):
        lstInd.append(2)
    
    if ('generacion' in lsCol):
        lstInd.append(3)
    
    if ('anio_mes' in lsCol):
        lstInd.append(4)
    

    # while (i < len(lsCol)):
    #     for j in lst:
    #         for k in lstTitulo:
    #             for l in lstInd:
    #                 if k[l] == k:
    #                     lstFinal.append(i[l])
                    
    #                 if j[i] == k:
    #                     item = j[i]
    #                     lstFinal.append(item)
    #     i += 1
    
    print(lstFinal)


def datos(lsArch: List) -> List:
    lsArch = lsArch[1:]
    lst = list()

    for i in lsArch:
        i = i[:-1]
        dato = i.split(",")
        dato[3] = int(dato[3])
        lst.append(dato)
    
    return lst

def titulo(lsArch: List) -> List:
    lsArch = lsArch[0]
    lst = list()
    lst.append(lsArch[:-1])
    
    return lst

def main():
    lsRes = []
    lsCol = ['fuente','region']
    lsArch = ['central,region,fuente,generacion,anio_mes\n', 'CAPE,COMAHUE,Termica,21868984,2020-01\n', 'AESP,BUENOS AIRES,Termica,193938412,2012-01\n', 'CAPE,COMAHUE,Termica,20009911,2017-03\n', 'ATUC,BUENOS AIRES,Nuclear,269321,2020-03\n', 'AMEGHI,PATAGONICA,Hidraulica,11705,2018-08\n', 'ANAT,NOROESTE,Termica,7670154,2018-07\n',
              'APAR,BUENOS AIRES,Termica,1077474,2015-09\n', 'ARAUEO,NOROESTE,Renovable,844759,2017-02\n', 'ARROHI,COMAHUE,Hidraulica,2961,2012-01\n', 'ATUC,BUENOS AIRES,Nuclear,237003,2019-03\n', 'ULN1FV,CUYO,Renovable,5779081,2020-03\n', 'APAR,BUENOS AIRES,Termica,43969,2020-02\n', 'VLONEO,BUENOS AIRES,Renovable,1171872,2020-02\n']
    lsDominio(lsArch, lsCol, lsRes)
    # print(lsRes)


main()