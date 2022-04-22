def leerArchivo():
    arch = open("/Users/tomasprodan/Documents/Info GRAL/Practica 7/7.2/7.2.csv", "r")
    lst = []
    suma = int()
    cont = 0
    for linea in arch:
        linea = linea[:-1]
        linea = linea.split(",")
        lst.append(linea)
    arch.close()
    
    for i in range(0, len(lst)):
        for j in range(0, len(lst[i])):
            while cont < len(lst[i]):
                # print(lst[i][j])
                suma += int(lst[i][j])
                cont += 1
    print(suma)
    # print(lst[1])
    # print(lst[2])
    # print(suma)
leerArchivo()

'''
lst[0][0]
lst[0][1]
lst[0][2]
lst[0][3]

chequeo si i == "\n"
    if true
        cont += 1

lst[1][0]
lst[1][1]
lst[1][2]
lst[1][3]
lst[1][4]




'''