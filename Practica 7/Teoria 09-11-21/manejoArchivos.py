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

def mostrarPersonas(di):
    i = 0
    lstClaves = list(di.keys())
    titulo = "{:<5s} {:.12s} {:.12s} {:5s} {:.5s} {:.5s}".format("DNI","APELLIDO","NOMBRE","PP1","PP2","PP3")
    print(titulo)
    print()
    while i<len(di):
        clave = lstClaves[i]
        lstValor = di[clave]
        nom = lstValor[1]
        ape = lstValor[0]
        lstNotas = lstValor[2]
        fila = "{:<5d} {:.12s} {:.12s} {:5s} {:.5s} {:.5s}".format(clave, ape, nom, lstNotas[0], lstNotas[1], di[clave][2][2])
        print(fila)
        i += 1

def main():
    di = {}
    cargarPersonas("/Users/tomasprodan/Documents/Info GRAL/Practica 7/Teoria 16-11-21/datos.csv", di)
    mostrarPersonas(di)
main()

