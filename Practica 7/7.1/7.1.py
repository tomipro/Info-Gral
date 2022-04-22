def insertionSort(lst):
    for i in range(1, len(lst)):
        a = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > a:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = a

def ordenar(lst):
    for i in range(len(lst) - 1):
        for j in range(0, len(lst)-i-1):
            if lst[j] > lst[j + 1]:
                aux = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = aux


def informe(arch):
    archivo = open(arch, "r")
    lst = [float(linea[:-1]) for linea in archivo]
    archivo.close()
    ordenar(lst)
    return lst

def suma(lst):
    suma = 0
    for num in lst:
        suma += num
    return suma

def main():
    arch = informe("/Users/tomasprodan/Documents/Info GRAL/Practica 7/7.1/7.1.txt")
    largo = len((arch))
    promedio = ((suma(arch))/largo)
    print(F"\nEl maximo es: {arch[-1]} | El minimo es: {arch[0]}\nEl promedio es: {promedio:.2f} | Existen {largo} lineas.\n")
main()