def cargar():
    archivo = open("/Users/tomasprodan/Documents/Info GRAL/Practica 7/7.7/7.7personas.csv", "r")
    dic = {}
    for linea in archivo:
        linea = linea.split(",")
        dic[int(linea[2])] = linea[0], linea[1]
    archivo.close()
    return dic

def agregarRegistro():
    dic = cargar()
    while True:
        try:
            dni = int(input("Ingrese DNI: "))
            if dni in dic:
                print("ERROR. DNI ya existe.\n")
                continue
        except ValueError:
            continue
        else:
            break
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    dic[dni] = [nombre, apellido]
    string = f"{nombre},{apellido},{str(dni)}\n"
    archivo = open("/Users/tomasprodan/Documents/Info GRAL/Practica 7/7.7/7.7personas.csv", "a")
    archivo.write(string)
    archivo.close()

def eliminarRegistro():
    dic = cargar()
    while True:
        try:
            dni = int(input("Ingrese DNI a eliminar: "))
            if dni not in dic:
                dni = input(print("ERROR. DNI no existe, desea ingresar nuevo DNI? (Y/N)\n"))
                if dni.lower() == "y":
                    agregarRegistro()
                    continue
                elif dni.lower() == "n":
                    break
                else:
                    dni = input(print("ERROR. Responda con \"Y\" (SI) o \"N\" (NO)"))
                    continue
        except ValueError:
            print("Valor ingresado no es numerico.")
            continue
        else:
            break
    dic.pop(dni, "")
    string = ""
    archivo = open("/Users/tomasprodan/Documents/Info GRAL/Practica 7/7.7/7.7personas.csv", "w")
    for key in dic:
        string += str(dic[key][0])+","+str(dic[key][1])+","+str(key)+'\n'
    archivo.write(string)
    archivo.close()

def DNIoApellido(x):
    for car in x:
        return False if (car >= "0" and car <= "9") else True

def buscarRegistro():
    dic = cargar()
    x = input("Ingrese DNI o apellido a buscar: ")
    if not DNIoApellido(x):
        dni = int(x)
        if dni in dic:
            print(f"\nNombre: {dic[dni][0]}\nApellido: {dic[dni][1]}\nDNI: {str(dni)}")
    else:
        apellido = x
        for key in dic:
            if (dic[key][1]) == apellido:
                print(f"\nNombre: {dic[key][0]}\nApellido: {dic[key][1]}\nDNI:{key}")

def ordenarArchivoPor():
    dic = cargar()
    lst = []
    for key in dic:
        lst.append([dic[key][0], dic[key][1], int(key)])
    x = int(input("Ordenar por: \n1.) Nombre\n2.) Apellido\n3.) DNI\n")) - 1
    for i in range(1, len(lst)):
        j = lst[i][x]
        k = i - 1
        while k >= 0 and lst[k][x] > j:
            lst[k + 1][x] = lst[k][x]
            k -= 1
        lst[k + 1][x] = j
    string=''
    for sublista in lst:
        string+=sublista[0]+','+sublista[1]+','+str(sublista[2])+'\n'
    file=open('/Users/tomasprodan/Documents/Info GRAL/Practica 7/7.7/7.7personas.csv','w')
    file.write(string)
    file.close()

def main():
    x=int(input("Ingrese opcion: "))
    while x<6:
        if x == 1:
            agregarRegistro()
        if x == 2:
            eliminarRegistro()
        if x == 3:
            buscarRegistro()
        if x == 4:
            ordenarArchivoPor()
        x=int(input("\nIngrese opcion: "))
main()