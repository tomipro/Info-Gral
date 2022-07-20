def prom(lst):
    suma = 0
    cant = len(lst)
    for num in lst:
        suma += num
    return (suma/cant)

def borrar(lst, prom):
    i = 0
    while i < len(lst):
        if lst[i] > prom:
            lst.remove(lst[i])
        else:
            i += 1
    return lst

def ordIns(lst):
    for i in range(1, len(lst)):
        a = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > a:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = a



def main():
    lista = [24, 30, 2, 10, 15, 6, 65, 42]
    pro = prom(lista)
    print(f"El valor promedio es {pro:.2f}")
    print(f"Lista original es {lista}")
    borrar(lista, pro)
    print(f"Lista modificada es {lista}")
    ordIns(lista)
    print(f"Lista modificada y ordenada es {lista}")
main()