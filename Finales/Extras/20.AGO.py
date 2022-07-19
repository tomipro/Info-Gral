def contagiados(fecha, lstCiudad, lstContagios):
    lstCiu = list()
    for i in lstCiudad:
        i = i[:-1]
        ciudad = i.split(",")
        ciudad[0] = int(ciudad[0])
        lstCiu.append(ciudad)

    lstCon = list()
    for j in lstContagios:
        j = j[:-1]
        dato = j.split(",")
        dato[0] = int(dato[0])
        dato[1] = int(dato[1])
        dato[2] = int(dato[2])
        dato[3] = int(dato[3])
        lstCon.append(dato)

    lst = list()
    lst0 = list()
    z = len(lstCiu) - 1
    for k in lstCon:
        contagiados = int()
        for l in lstCiu:
            if ((fecha == k[3]) and (l[0] == k[2])):
                nomCiudad = l[1]
                contagiados += 1
                tupla = (nomCiudad, contagiados)
                lst.append(tupla)

    lst2 = list()
    for m in lst:
        cont = int()
        for n in lst:
            if ((m[0] == n[0])):
                cont += m[1]
                tupla = (m[0], cont)
        if tupla not in lst2:
            lst2.append((m[0], cont))

    return lst2


def main():
    print("Prueba para el Ej01")
    lstciudad = ["223,Parana\n", "114,Merlo\n", "218,Guaymallen\n",
                 "132,C.Rivadavia\n", "341, Adolfo Alsina\n", "404, Jose C. Paz\n"]
    lstcontagios = ["10,33,114,200518\n", "11,31,223,200519\n", "12,27,218,200319\n", "13,26,132,200616\n", "14,74,341,200319\n", "15,62,404,200606\n",
                    "16,46,218,200709\n", "17,55,132,200630\n", "18,55,341,200612\n", "19,54,484,200701\n", "1,23,114,200315\n",
                    "2,55,223,200519\n", "3,34,218,200319\n", "4,33,132,200425\n", "5,27,341,200422\n", "6,21,404,200501\n", "7,31,114,200503\n", "8,44,114,200513\n", "9,44,218,200519\n"]
    print(contagiados(200519, lstciudad, lstcontagios))


main()
