from typing import List, Tuple


def aprobadas(lstAlumnos: List, lstMaterias: List, lstCursadas: List, nombreApellido: str) -> List[Tuple]:
    data = (datos(lstAlumnos, lstMaterias, lstCursadas))
    alum = data[0]
    mat = data[1]
    curs = data[2]
    nombres = list()

    matAprobadas = list()

    for i in mat:
        for j in curs:
            for k in alum:
                if (i[0] == j[0] and (j[2] >= 4) and k[1] == nombreApellido and j[1] == k[0]):
                    nomMat = i[1]
                    nota = j[2]
                    tupla = (nomMat, nota)
                    matAprobadas.append(tupla)

    return matAprobadas


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
    print(aprobadas(lstAlumnos, lstMaterias, lstCursadas, 'Ricardo Bochini'))


main()

'''
EJ01

Realice una función llamada aprobadas que reciba las 3 listas mencionadas y un string con el nombre y apellido de un
alumno, y que como resultado de su trabajo retorne una lista de tuplas donde conste el nombre de cada materia y la nota que
se sacó dicho alumno al aprobar esa cursada. La lista retornada debe tener una tupla por cada materia aprobada por ese
alumno y cada tupla debe contener en la posición [0] el nombre de la materia y en la posición [1] la nota obtenida en esa
materia por el alumno. Se consideran materias aprobadas a las que tienen nota mayor o igual a 4, y no deben incluirse en la
lista las materias no aprobadas.

Prueba para el EJ01:

[('Álgebra y Geometría', 6.0), ('Física I', 7.5), ('Informática Gral', 6.0)]
'''
