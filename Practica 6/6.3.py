def estaEnLista(num, lst):
    return num in lst

def vaciarLista(lst):
    while len(lst) != 0:
        lst.pop()

def cargarConjuntos(lst1, lst2):
    num = int(input("Ingresar numeros, 0 (cero) para terminar: "))
    lista = []
    while num != 0:
        if num<0:
            print("Error. Numero no positivo.")
        else:
            print("Error, numero repetido. ") if (estaEnLista(num, lista)) else lista.append(num)
        num = int(input())

def cargarConj(lst1, lst2):
    vaciarLista(lst1)
    vaciarLista(lst2)
    print("Ingrese lista 1: ")
    cargarConjuntos(lst1)
    print("Ingrese lista 2: ")
    cargarConjuntos(lst2)

def union_(a, b):
    #metodo 1:
    # a,b = set(a), set(b)
    # return (a | b)
    #metodo 2:
    temp = []
    for i in a:
        if not estaEnLista(i, temp):
            temp.append(i)
    for i in b:
        if not estaEnLista(i, temp):
            temp.append(i)
    return temp
def interseccion(a, b):
    #metodo 1:
    # return [i for i in a if i in b]
    #metodo 2:
    # a,b = set(a), set(b)
    # return list(a & b)
    #metodo 3:
    temp = []
    for i in a:
        if i in b and not estaEnLista(i, temp):
            temp.append(i)
    return temp
def diferencia(a, b):
    # metodo 1:
    # a = set(a)
    # b = set(b)
    # return list(a-b)
    #metodo 2:
    #return [i for i in a if not i in b]
    # metodo 3:
    temp = []
    for i in a:
        if i not in b and not estaEnLista(i, temp):
            temp.append(i)
    return temp
def diferenciaSimetrica(a,b):
    # union sin la interseccion
    # metodo 1:
    # return list(set(union_(a, b)) - set(interseccion(a,b)))
    #metodo 2:
    temp = []
    for i in a:
        if i not in b and not estaEnLista(i, temp):
            temp.append(i)
    for i in b:
        if i not in a and not estaEnLista(i, temp):
            temp.append(i)
    return temp

def menu():
    print("1. CARGAR CONJUNTOS")
    print("2. UNIÓN")
    print("3. INTERSECCIÓN")
    print("4. DIFERENCIA (A-B)")
    print("5. DIFERENCIA SIMÉTRICA")
    print("6. SALIR")
    print("Ingrese el valor de la opción: ", end = "")
    val = int(input())
    while val < 0 or val > 6:
        val = int(input("Error. Ingrese valor entre 1 y 6."))
    return val

def control(val, lst1, lst2):
    if val == "1":
        cargarConjuntos(lst1, lst2)
        print("\nEl conjunto 1 contiene \n",lst1, end = "\n")
        print("\nEl conjunto 2 contiene \n",lst2, end = "\n")
    elif val == "2":
        print(union_(lst1, lst2))
        print("Disparando funcion union")
    elif val == "3":
        print(interseccion(lst1, lst2))
        print("Disparando funcion interseccion")
    elif val == "4":
        print(diferencia(lst1, lst2))
        print("Disparando funcion diferencia")
    elif val == "5":
        print(diferenciaSimetrica(lst1, lst2))
        print("Disparando funcion diferencia simetrica")
    elif val == "6":
        print("Chau. Saliendo.")
    
# def main():
#     val = menu()
#     while (val != "6"):
#         control(val)
#         print()
#         val = menu()
# main()
def main():
    lst1 = []
    lst2 = []
    val = menu()
    while val != 6:
        control(val, lst1, lst2)
        val = menu()
main()