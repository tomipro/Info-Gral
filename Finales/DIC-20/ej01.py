from typing import List, NoReturn, Tuple

def bubbleSort(lst: List) -> None:
    n = len(lst)
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if lst[j][1] < lst[j + 1][1]:#[1] es para ordenar por cantidad
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp

def media_01(n: int, lstCiudad: List, lstResiduos: List) -> Tuple:
    ciudad = list()
    for i in lstCiudad:
        dato = i.split(",")
        dato[0] = int(dato[0])
        dato[1] = dato[1][:-1]
        ciudad.append(dato)
    res = list()
    for j in lstResiduos:
        dato = j.split(",")
        dato[0] = int(dato[0])
        dato[1] = int(dato[1])
        dato[2] = int(dato[2])
        res.append(dato)
    resTot = int()
    lst = list()
    cont = int()
    for k in ciudad:
        id_ciudad = k[0]
        nom_ciudad = k[1]
        residuos = int()
        fecha = int()
        for l in res:
            if l[1] == id_ciudad:
                cont += 1 #cantidad de ciudades
                residuos += l[0] #cantidad total de residuos para dicha ciudad
                fecha += 1 #dias
        resTot += residuos
        promedio = residuos / fecha
        lst.append([nom_ciudad, round(promedio, 1)])
    promTot = round((resTot / cont), 2)
    bubbleSort(lst)
    lstFinal = list()
    for w in lst:
        if len(lstFinal) < n: 
            lstFinal.append(w)
    return (promTot, lstFinal)

def main():
    print("Prueba para el EJ01")
    lstCiudad = ['223,Parana\n', '114,Merlo\n', '218,Guaymallen\n', '132,C. Rivadavia\n', '341,Adolfo Alsina\n', '404,Jose C. Paz\n']
    lstResiduos = ['33,114,200518\n', '31,223,200519\n', '27,218,200319\n', '26,132,200616\n', '74,341,200319\n', '62,404,200606\n', '46,218,200709\n', '55,132,200630\n', '55,341,200612\n', '54,404,200701\n', '23,114,200315\n', '55,223,200519\n', '34,218,200319\n', '33,132,200425\n', '27,341,200422\n', '21,404,200501\n', '31,114,200503\n', '44,114,200513\n', '44,218,200519\n']
    print(media_01(6,lstCiudad ,lstResiduos))
main()