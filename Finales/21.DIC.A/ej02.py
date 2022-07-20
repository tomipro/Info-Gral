def segmentos(lstAlumnos, lstMaterias, lstCursadas):
    alum = []
    for i in lstAlumnos:
        dato = i.split(",")
        dato[0] = int(dato[0])
        dato[1] = dato[1][:-1]
        alum.append(dato)
    mat = []
    for j in lstMaterias:
        dato = j.split(",")
        dato[0] = int(dato[0])
        dato[1] = dato[1][:-1]
        mat.append(dato)
    curs = []
    for k in lstCursadas:
        dato = k.split(",")
        dato[0] = int(dato[0])
        dato[1] = int(dato[1])
        dato[2] = float(dato[2])
        curs.append(dato)
    clave = ["M", "R", "B", "E"]
    m = []
    r = []
    b = []
    e = []
    dic = {}
    for x in curs:
        id_mat = x[0]
        id_alum = x[1]
        nota = x[2]
        if nota < 4:
            m.append(nota)
        elif nota >= 4 and nota < 7:
            r.append(nota)
        elif nota >= 7 and nota < 8:
            b.append(nota)
        elif nota >= 8 and nota <= 10:
            e.append(nota)
    # for y in lstMaterias:
        
    # for c in clave:
    #     dic[c][0] = 

                    

        
def main():
    print("Prueba para el EJ02")
    lstAlumnos = ['152002,Juan Gonzalez\n','152001,Ana Martinez\n','151988,Ricardo Bochini\n','180372,Vicente Pernia\n']
    lstMaterias = ['132,Informática Gral\n', '127,Álgebra y Geometría\n', '137,Física I\n']
    lstCursadas = ['137,152001,4.0\n', '127,151988,6.0\n', '137,151988,7.5\n' ,'132,152002,2.0\n', '132,151988,6.0\n', '127,152001,2.0\n', '127,180372,10.0\n']
    print(segmentos(lstAlumnos, lstMaterias, lstCursadas))
main()


"""
clave: 

materia <- id_materia
nombre alum 



"""