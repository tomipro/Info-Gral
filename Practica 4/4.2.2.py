# def main():
#     cont = 0
#     n = int(input("Ingrese numeros enteros positivos (finalice con 0): "))
#     while n != 0:
#         if cont == 0:
#             may = n
#             men = n
#             cont += 1
#         if n < men:
#             men = n
#         if n > may:
#             may = n
#         n = int(input("Ingrese numeros enteros positivos (finalice con 0): "))
#     if n == 0 and cont > 0:
#         print("El mayor es {} y el menor es {}".format(may, men))
# main()
def ordenar(lst):
    for i in range(1, len(lst)):
        a = lst[i]
        j = i - 1
        while j >=0 and lst[j] > a:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = a
    return lst

def imprimir(lst):
    menor = lst[0]
    mayor = lst[-1]
    print("\nMenor: {}\nMayor: {}\n".format(menor, mayor))

def main():
    lst = []
    n = None
    while n != 0:
        n = int(input("Ingrese numero: "))
        if n != 0:
            lst.append(n)
    if lst != []:
        lst = ordenar(lst)
        imprimir(lst)
main()

