def sumatoria(a, b):
    suma = 0
    for i in range(a, b+1):
        suma += i
    return suma
def main():
    a = int(input("Ingrese primer numero: "))
    b = int(input("Ingrese segundo numero: "))
    print("Resultado: {}".format(sumatoria(a, b)))
main()