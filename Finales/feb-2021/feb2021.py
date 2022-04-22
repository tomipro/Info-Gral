def menor(lst):
    pass

def minimos(lstEnergia):
    # lstAux = []
    # for linea in lstEnergia:
    #     linea = linea[:-1]
    #     if linea not in lstAux:
    #         lstAux.append(linea)
    lstAux = []
    for i in lstEnergia:
        datos = i.split(",")
        datos[0] = int(datos[0])
        datos[1] = int(datos[1])
        datos[2] = float(datos[2])
        lstAux.append(datos)
    return lstAux


def main():
    print("Prueba para el EJ01")
    lstEnergia = ['101205,1,24.2\n', '110607,8,54.4\n', '120318,3,18.1\n',
    '090501,9,88.4\n', '101209,1,26.8\n', '101217,3,22.4\n', '190101,8,44.0\n']
    print(minimos(lstEnergia))
main()