def cargarLocal():
    arch = open("/Users/tomasprodan/Documents/Info GRAL/Practica 7/7.8/localidades.csv", "r")
    dic = {}
    for linea in arch:
        linea = linea.split(",")
        linea[0] = int(linea[0])
        linea[2] = int(linea[2])
        linea[3] = int(linea[3])
        linea[4] = int(linea[4])
        dic[linea[0]] = [linea[1], linea[2], linea[3], linea[4]]        
    arch.close()
    return dic

def cargarProv():
    arch = open("/Users/tomasprodan/Documents/Info GRAL/Practica 7/7.8/provincias.csv", "r")
    dic = {}
    for linea in arch:
        linea = linea.split(",")
        linea[0] = int(linea[0])
        linea[2] = int(linea[2])
        dic[linea[0]] = [linea[1], linea[2]]
    arch.close()
    return dic

def cargarPais():
    arch = open("/Users/tomasprodan/Documents/Info GRAL/Practica 7/7.8/paises.csv", "r")
    dic = {}
    for linea in arch:
        linea = linea.split(",")
        linea[0] = int(linea[0])
        linea[2] = int(linea[2])
        dic[linea[0]] = [linea[1], linea[2]]
    arch.close()
    return dic

def poblacion(id_provincia):
    dicProv = cargarProv()
    dicLocal = cargarLocal()
    pob = int()
    for i in dicLocal:
        if dicLocal[i][1] == id_provincia:
            pob += dicLocal[i][3]
    print(pob, dicProv[id_provincia][0])

def localidadMaxima():
    dicProv = cargarProv()
    dicLocal = cargarLocal()
    dicPais = cargarPais()
    maximo = int()
    for i in dicLocal:
        if dicLocal[i][3] > maximo:
            maximo = dicLocal[i][3]
            id_maximo = i
    id_provincia = dicLocal[id_maximo][1]
    id_pais = dicProv[id_provincia][1]
    print(maximo)
    print(dicLocal[id_maximo][0])
    print(dicProv[id_provincia][0])
    print(dicPais[id_pais][0])

def main():
    n = int(input("Ingrese ID de provincia: "))
    # poblacion(n)
    localidadMaxima()

main()

"""
ID_localidad (entero)
nombre (cadena de caracteres)
ID_provincia (entero)
superficie (entero)
poblacion (entero)

meto id de provincia -> dicProv[0] y dicLocal[2]
me devuelve poblacion y nombre de provincia {
    if input==dicLocal[2] -> retorno dicProv[1] y dicLocal[4]
}
"""