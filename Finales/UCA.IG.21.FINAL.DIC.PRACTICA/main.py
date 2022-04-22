# def maximo(lsArch, n):

#     pass

def cargarPersonas(lsArch):
    di = {}
    lst = []
    i = 0
    for linea in lsArch:
        linea = linea[:-1]
        linea = linea.split(",")
        lst.append(linea)
    lst = lst[1:-1]
    for j in lst:
        clave = lst[i][4]
        valor = [int(lst[i][3]), lst[i][0]]
        di[clave] = valor
        i += 1
    # print(di)
    q = 0
    aa = []
    mm = []
    fechas = list(di.keys())
    print(fechas)
    for u in range(len(fechas)):
        for w in range(u+1, len(fechas)):
            if fechas[0][u] < fechas[0][w]:
                aux = fechas[u]
                fechas[u] = fechas[w]
                fechas[w] = aux
    print(fechas)
    # for z in fechas:
    #     x = fechas[u].split("-")
    #     anios = x[0]
    #     meses = x[1]
    #     aa.append(anios)
    #     mm.append(meses)
    #     u += 1
    # # print(x)
    # print(aa)
    # print(mm)
    # aa = []
    # a = 0
    # for k in fechas:


    #     aa.append(fechas)
    #     a += 1
    # print(aa)
    # print(fechas)
    # print(fechas)
    # print(fechas[0].split("-"))
    # ordenarLista(fechas)
    # print(fechas)
    
    # lstClave = list(di.keys())
    # ls1 = list(di.values())
    # x = 0
    # aamm = []
    # for k in lst:
    #     anomes = (lst[x][2]).split("-")
    #     aamm.append(anomes)
    #     x += 1
    # print(aamm)


    # for linea in lsArch:
    #     linea = linea[1:-1]
    #     lstLinea = linea.split(",")
    #     clave = lstLinea[0]
    #     valor = [(lstLinea[3]), lstLinea[4]]
    #     di[clave] = valor
    # # di.pop("central")
    # return di


def ordenarLista(lst):
    for i in range(0, len(lst) - 1):
        for j in range(0, len(lst)):
            if lst[i] > lst[i]:
                aux = lst[i]
                lst[i] = lst[j]
                lst[j] = aux
# def titulo(lsArch):
#     lst = []
#     for linea in lsArch:
#         linea = linea[:-1]
#         lst.append(linea)
#     dic = {}
#     for linea in lst:
#         linea = linea.split(",")
#         dic[linea[0]] = (linea[3]), linea[4]
#     clave = 

#     return dic

def aDic(lsArch):
    di = {}


def main():
    lsArch=['central,region,fuente,generacion,anio_mes\n','CAPE,COMAHUE,Termica,21868984,2020-01\n','AESP,BUENOS AIRES,Termica,193938412,2012-01\n','CAPE,COMAHUE,Termica,20009911,2017-03\n','ATUC,BUENOS AIRES,Nuclear,269321,2020-03\n','AMEGHI,PATAGONICA,Hidraulica,11705,2018-08\n','ANAT,NOROESTE,Termica,7670154,2018-07\n','APAR,BUENOS AIRES,Termica,1077474,2015-09\n','ARAUEO,NOROESTE,Renovable,844759,2017-02\n','ARROHI,COMAHUE,Hidraulica,2961,2012-01\n','ATUC,BUENOS AIRES,Nuclear,237003,2019-03\n','ULN1FV,CUYO,Renovable,5779081,2020-03\n','APAR,BUENOS AIRES,Termica,43969,2020-02\n','VLONEO,BUENOS AIRES,Renovable,1171872,2020-02\n']
    n = 0
    print(cargarPersonas(lsArch))
    # print(titulo(lsArch))
    # maximo(lsArch, n)
    # print("Para n =", n)
main()

