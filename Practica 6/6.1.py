def estaEnLista1(num, lst):
    return num in lst
def estaEnLista2(num, lst):
    x = False
    for i in lst:
        if num == i:
            x = True
            i += 1
    return x
def estaEnLista3(num,lst):
    c = 0
    x = False
    while c<len(lst):
        if lst[c] == num:
            x = True
        c+=1
def ingreso():
    lista = []
    num = int(input("Ingrese numeros, 0 para terminar el ingreso: "))
    while num != 0:
        if num<0:
            print("Error. Numero negativo.")
        else:
            print("Error, numero repetido. ") if (estaEnLista1(num,lista) or estaEnLista2(num,lista) or estaEnLista3(num,lista)) else lista.append(num)
        num = int(input())
    return lista
def main():
    lst = ingreso()
    print(lst)
main()