import math
def validarT1(num):
    largo = int(math.log10(num))
    x = int(num // math.pow(10, largo))
    y = int(num % 10)
    centro = int(num % math.pow(10, largo)) // 10
    centroDigs = centro % 10
    suma = 0
    while num != 0:
        suma += centroDigs
        num = num // 10
        centroDigs = num % 10
    print(x*y, suma)

def main():
    # num = int(input("Ingrese numero: "))
    print(validarT1(523412))
main()