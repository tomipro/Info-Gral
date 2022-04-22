def estaEnLista(num, lst):
    return num in lst
def cargarLista():
    lista = []
    num = int(input("Ingrese numeros, 0 (cero) para terminar: "))
    while num != 0:
        if num<0:
            print("Error. Numero no positivo. ")
        else:
            print("Error. Numero repetido. ") if (estaEnLista(num, lista)) else lista.append(num)
        num = int(input())
    return lista
def main():
    lst = cargarLista()
    print(lst)
main()