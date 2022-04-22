def bubbleSort(lst):
    n = len(lst)
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if lst[j] < lst[j + 1]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp
                
def maximo(lsArch, n):
    lstTit = titulos(lsArch)
    lstDato = datos(lsArch)
    lstFecha = list()
    lstGen = list()
    for i in lstDato:
        lstFecha.append(i[4])
        lstGen.append(i[3])
    bubbleSort(lstFecha)
    bubbleSort(lstDato)
    lstGen = lstGen[:n]
    lstAux = list()
    lstAux2 = list()
    for j in lstDato:
        for k in lstGen:
            if j[3] == k:
                central = j[0]
                gen = j[3]
                fecha = j[4]
                lstAux.append(fecha)
                lstAux2.append((central, gen, fecha))
                bubbleSort(lstAux)
    for i in lstAux:
        for j in lstAux2:
            if i == j[2]:
                print(j[0], j[1], j[2])

def titulos(lst):
    titulo = list()
    for i in lst:
        dato = i.split(",")
        dato = i[:-1]
        titulo.append(dato)
    # titulo = titulo[0]
    return titulo[0]

def datos(lst):
    aux = list()
    for i in lst:
        i = i[:-1]
        dato = i.split(",")
        aux.append(dato)
    lstDatos = aux[1:]
    for j in lstDatos:
        j[3] = int(j[3])
    return lstDatos



def main():
    lsArch=['central,region,fuente,generacion,anio_mes\n','CAPE,COMAHUE,Termica,21868984,2020-01\n','AESP,BUENOS AIRES,Termica,193938412,2012-01\n','CAPE,COMAHUE,Termica,20009911,2017-03\n','ATUC,BUENOS AIRES,Nuclear,269321,2020-03\n','AMEGHI,PATAGONICA,Hidraulica,11705,2018-08\n','ANAT,NOROESTE,Termica,7670154,2018-07\n','APAR,BUENOS AIRES,Termica,1077474,2015-09\n','ARAUEO,NOROESTE,Renovable,844759,2017-02\n','ARROHI,COMAHUE,Hidraulica,2961,2012-01\n','ATUC,BUENOS AIRES,Nuclear,237003,2019-03\n','ULN1FV,CUYO,Renovable,5779081,2020-03\n','APAR,BUENOS AIRES,Termica,43969,2020-02\n','VLONEO,BUENOS AIRES,Renovable,1171872,2020-02\n']
    n = 0
    print("Para n =", n)
    print(maximo(lsArch, n))
    datos(lsArch)
main()


'''
columnas: 
    central
    generacion
    anio mes


'''