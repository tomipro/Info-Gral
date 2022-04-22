def leerArchivo():
    archivo = open("/Users/tomasprodan/Documents/Info GRAL/Practica 7/7.2/7.2.csv", "r")
    lst = [linea.split(",") for linea in archivo]
    lst = [linea[:-1] for linea in lst]
    archivo.close()
    return lst
print(leerArchivo())

# def escribirArchivo(lst):
#     archivo = open("/Users/tomasprodan/Documents/Info GRAL/Practica 7/7.2.py/7.2-despues.csv", "w")
#     contenido = leerArchivo()
#     contenido += promedio(lst)
#     archivo.write(contenido)
#     archivo.close()
