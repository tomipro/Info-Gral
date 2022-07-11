from typing import Dict, List


def segmentos(lstAlumnos: List, lstMaterias: List, lstCursadas: List) -> Dict:
    data = (datos(lstAlumnos, lstMaterias, lstCursadas))
    alum = data[0]
    mat = data[1]
    curs = data[2]
    dic = {}

    matM = list()
    matR = list()
    matB = list()
    matE = list()

    for i in mat:
        for j in curs:
            for k in alum:
                nomAlum = k[1]
                nomMat = i[1]
                nota = j[2]
                res = [nomMat, nomAlum]
                if ((j[1] == k[0]) and (j[2] < 4) and (i[0] == j[0])):
                    matM.append(res)
                    dic['M'] = matM
                elif ((j[1] == k[0]) and (j[2] >= 4) and (j[2] < 7) and (i[0] == j[0])):
                    matR.append(res)
                    dic['R'] = matR
                elif ((j[1] == k[0]) and (j[2] >= 7) and (j[2] < 8) and (i[0] == j[0])):
                    matB.append(res)
                    dic['B'] = matB
                elif ((j[1] == k[0]) and (j[2] >= 8) and (j[2] <= 10) and (i[0] == j[0])):
                    matE.append(res)
                    dic['E'] = matE

    return dic


def datos(lstAlumnos: List, lstMaterias: List, lstCursadas: List) -> List[List]:
    alum = list()
    mat = list()
    curs = list()

    for i in lstAlumnos:
        i = i[:-1]
        dato = i.split(",")
        dato[0] = int(dato[0])
        alum.append(dato)

    for j in lstMaterias:
        j = j[:-1]
        dato = j.split(",")
        dato[0] = int(dato[0])
        mat.append(dato)

    for k in lstCursadas:
        k = k[:-1]
        dato = k.split(",")
        dato[0] = int(dato[0])
        dato[1] = int(dato[1])
        dato[2] = float(dato[2])
        curs.append(dato)

    return [alum, mat, curs]


def main():
    print("Prueba para el EJ01")
    lstAlumnos = ['152002,Juan Gonzalez\n', '152001,Ana Martinez\n',
                  '151988,Ricardo Bochini\n', '180372,Vicente Pernia\n']
    lstMaterias = ['132,Informática Gral\n',
                   '127,Álgebra y Geometría\n', '137,Física I\n']
    lstCursadas = ['137,152001,4.0\n', '127,151988,6.0\n', '137,151988,7.5\n', '132,152002,2.0\n',
                   '132,151988,6.0\n', '127,152001,2.0\n', '127,180372,10.0\n']
    print(segmentos(lstAlumnos, lstMaterias, lstCursadas))


main()


'''
EJ02
Realice una función llamada segmentos que reciba las 3 listas mencionadas. Como resultado de su trabajo la función deberá
retornar un diccionario con cuatro claves y cuyos valores de cada clave sea una lista donde cada ítem de la lista será una
sublista compuesto por el nombre de una materia y el nombre un estudiante de acuerdo al siguiente criterio que se detalla a
continuación:

    1. clave -> 'M' valores -> sublista con el nombre de la materia y el nombre del estudiante si el estudiante obtuvo una
    nota menor estrictamente a 4.0
    2. clave -> 'R' valores -> sublista con el nombre de la materia y el nombre del estudiante si el estudiante obtuvo una
    nota mayor o igual a 4.0 y menor estrictamente a 7.0
    3. clave -> 'B' valores -> sublista con el nombre de la materia y el nombre del estudiante si el estudiante obtuvo una
    nota mayor o igual a 7.0 y menor estrictamente a 8.0
    4. clave -> 'E' valores -> sublista con el nombre de la materia y el nombre del estudiante si el estudiante obtuvo una
    nota mAyor o igual a 8.0 y menor o igual a 10.0

Prueba para el EJ02:

{'M': [['Informática Gral', 'Juan Gonzalez'], ['Algebra y Geometría', 'Ana Martinez']], 'R': [['Física
I', 'Ana Martinez'], ['Algebra y Geometría', 'Ricardo Bochini'], ['Informática Gral', 'Ricardo Bochini']],
'B': [['Física I', 'Ricardo Bochini']], 'E': [['Algebra y Geometría', 'Vicente Pernia']]}

'''
