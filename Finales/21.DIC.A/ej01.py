def aprobadas(lstAlumnos, lstMaterias, lstCursadas, nombre):
    alum = list()
    for i in lstAlumnos:
        dato = i.split(",")
        dato[0] = int(dato[0])
        dato[1] = dato[1][:-1]
        alum.append(dato)
    # print(alum)
    mat = list()
    for j in lstMaterias:
        dato = j.split(",")
        dato[1] = dato[1][:-1]
        dato[0] = int(dato[0])
        mat.append(dato)
    curs = list()
    for k in lstCursadas:
        dato = k.split(",")
        dato[0] = int(dato[0])
        dato[1] = int(dato[1])
        dato[2] = float(dato[2])
        curs.append(dato)
    info = list()
    for a in alum:
        id_alum = a[0]
        nomb_alum = a[1]
        for m in mat:
            id_mat = m[0]
            nom_mat = m[1]
            for c in curs:
                nota = c[2]
                if id_alum == c[1] and nota >= 4 and id_mat == c[0] and nombre == nomb_alum:
                    info.append((nom_mat, nota))
    # for x in curs:
    #     id_mat = x[0]
    #     id_alum = x[1]
    #     nota = x[2]
    #     for z in alum:
    #         if (nota >= 4) and (id_alum == z[0]):
    #             for y in mat:
    #                 nomMat = y[1]
    #                 if (y[0] == id_mat):
    #                     tupla = (nomMat, nota)
    #                     info.append(tupla)
    return info

def main():
    print("Prueba para el EJ01")
    lstAlumnos = ['152002,Juan Gonzalez\n','152001,Ana Martinez\n','151988,Ricardo Bochini\n','180372,Vicente Pernia\n']
    lstMaterias = ['132,Informática Gral\n', '127,Álgebra y Geometría\n', '137,Física I\n']
    lstCursadas = ['137,152001,4.0\n', '127,151988,6.0\n', '137,151988,7.5\n' ,'132,152002,2.0\n', '132,151988,6.0\n', '127,152001,2.0\n', '127,180372,10.0\n']
    print(aprobadas(lstAlumnos ,lstMaterias ,lstCursadas,'Ricardo Bochini'))
main()