def media_02(lstResiduos):
    res = list()
    for i in lstResiduos:
        linea = i.split(",")
        linea[0] = int(linea[0])
        linea[1] = int(linea[1])
        linea[2] = int(linea[2])
        res.append(linea)
    dic = {}
    for j in res:
        basura = j[0]
        id_ciudad = j[1]
        fecha = j[2]
        anio = fecha // 10000
        mes = (fecha // 100) % 100
        if mes not in dic:
            residuos = 0
            cont = 0
            for k in res:
                if (mes == ((k[2] // 100) % 100)):
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
    print(media_02(lstResiduos ))
main()