import math


def validar(num):
    largo = int(math.log10(num))
    izq = int(num // math.pow(10, largo))
    der = int(num % 10)
    # puede ser q termine en 0 y por eso agarro ultimos 2 digitos ponele
    if der == 0:
        der = int(num // math.pow(10, 1))
        der = int(der % 10) * 10
    centrales = int(num % (math.pow(10, largo))) // 10
    multiplicados = izq * der
    centralesDiv = centrales % multiplicados
    return True if ((multiplicados != 0) and (centralesDiv == 0)) else False


def main():
    num = int(input("Ingrese numero: "))
    print(validar(num))


main()
