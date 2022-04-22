def cargarPersonas(nomArch, di):
    arch = open(nomArch, "r")
    
    for linea in arch:
        linea = linea[:-1]
        lstLinea = linea.split(",")
        lstLinea[0] = int(lstLinea[0])
        clave = lstLinea[0]
        valor = [lstLinea[1], lstLinea[2], [lstLinea[3], lstLinea[4], lstLinea[5]]]
        di[clave] = valor
    arch.close()

def ordenar(lst):
    for i in range(1, len(lst)):
        a = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > a:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = a

def grabarArchivoOrdenadoDNI(nomArch, di):
    arch = open(nomArch, "w")
    lstClave = list(di.keys())
    ordenar(lstClave)
    for clave in lstClave:
        linea = str(clave)+","+di[clave][0]+","+di[clave][1]
        linea = linea + ","+di[clave][2][0]+ ","+di[clave][2][1]+ ","+di[clave][2][2]
        linea = linea + "\n"
        arch.write(linea)
    arch.close()

def mostrarPersonas(di):
    i = 0
    lstClaves = list(di.keys())
    titulo = "{:<5s} {:12s} {:12s} {:5s} {:5s} {:5s}".format("DNI","APELLIDO","NOMBRE","PP1","PP2","PP3")
    print(titulo)
    print()
    while i<len(di):
        clave = lstClaves[i]
        lstValor = di[clave]
        nom = lstValor[1]
        ape = lstValor[0]
        lstNotas = lstValor[2]
        fila = "{:<5d} {:12s} {:12s} {:5s} {:5s} {:5s}".format(clave, ape, nom, lstNotas[0], lstNotas[1], di[clave][2][2])
        print(fila)
        i += 1

def main():
    di = {}
    cargarPersonas("/Users/tomasprodan/Documents/Info GRAL/Practica 7/Teoria 16-11-21/datos.csv", di)
    mostrarPersonas(di)
    grabarArchivoOrdenadoDNI("/Users/tomasprodan/Documents/Info GRAL/Practica 7/Teoria 16-11-21/datosOrd.txt", di)
main()

