from random import randint as ri
def cargarListaAleatoria(a, b, can):
    lista = []
    if a > b:
        mayor = a
        menor = b
    else:
        mayor = b
        menor = a
    for i in range(can):
        num = ri(menor, mayor)
        lista.append(num)
    return lista

def fun1(lista):
    if lista != []:
        print(f"El minimo es {min(lista)} y el maximo es {max(lista)}")
    else:
        print("Lista vacia.")

def fun2(lista):
    lista = sorted(lista)
    max_ = lista[-1]
    min_ = lista[0]
    print(max_, min_)

def fun3(lista):
    if len(lista) == 0:
        return 0
    temp_max_ = lista[0]
    for i in lista:
        if i > temp_max_:
            temp_max_ = i
    return temp_max_

def fun4(lista):
    if len(lista) == 0:
        return 0
    temp_min_ = lista[0]
    for i in lista:
        if i < temp_min_:
            temp_min_ = i
    return temp_min_

def main():
    a = int(input("Ingrese primer extremo: "))
    b = int(input("Ingrese segundo extremo: "))
    can = int(input("Ingrese cantidad: "))
    cla = cargarListaAleatoria(a, b, can)
    print(cla)
    fun1(cla)
    fun2(cla)
    print(fun3(cla))
    print(fun4(cla))
main()
