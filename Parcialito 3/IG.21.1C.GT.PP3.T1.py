def mostrar(lst, n):
    menores = []
    i = 0
    while i < len(lst):
        minimo = 0
        for i in range(n):
            for num in lst:
                if num not in lst and (minimo == 0 or num < minimo):
                    minimo = num
            menores.append(minimo)
            minimo = 0
    return menores
    #mal sin terminar 

def main():
    lista = [12, 100, 5, 23, 65, 34]
    n = 10
    print(mostrar(lista, n))
main()