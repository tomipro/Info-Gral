def ordenar(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if lst[j] > lst[j + 1]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp

def main():
    lst = []
    num = int(input("Ingrese numero entero y positivo (0 para terminar): "))
    while (num != 0):
        if (num > 0):
            lst.append(num)
        else:
            num = int(input("Error. Ingrese entero POSITIVO (0 para terminar): "))
        num = int(input("Ingrese numero (0 para terminar): "))
    ordenar(lst)
    print(lst)
main()
