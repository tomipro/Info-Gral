def esLetra(c):
    return True if ((c >= "a" and c <= "z") or (c >= "A" and c <="Z")) else False

def leerArchivo(nombArch):
    strCuento = ""
    arch = open(nombArch, "r")
    for linea in arch:
        strCuento += linea
    arch.close()
    return strCuento

def palabrasADiccionario(strCuento, dicPal):
    i = 0
    palAux = ""
    while i < len(strCuento):
        palAux = ""
        while i < len(strCuento) and not esLetra(strCuento[i]):
            i += 1
        while i < len(strCuento) and esLetra(strCuento[i]):
            palAux += strCuento[i]
            i += 1
        if palAux != "":
            if dicPal.get(palAux) == None:
                dicPal[palAux] = 1
            else:
                dicPal[palAux] = dicPal[palAux] + 1

def crearArchFrecuencias(dicPal, nombArch):
    arch = open(nombArch, "w")
    for clave in dicPal:
        strLinea = clave + ", " + str(dicPal[clave]) + "\n"
        arch.write(strLinea)
    arch.close()

def frecuenciaPalabras(nombArch):
    dicPal = {}
    strCuento = leerArchivo(nombArch)
    palabrasADiccionario(strCuento, dicPal)
    crearArchFrecuencias(dicPal, "/Users/tomasprodan/Documents/Info GRAL/Practica 7/7.3.2/frecuencias7.3.2.csv")

def main():
    frecuenciaPalabras("/Users/tomasprodan/Documents/Info GRAL/Practica 7/7.3.2/7.3.2.txt")
main()
