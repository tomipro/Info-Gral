def dosPares(num):
    cont = 0
    while num > 0:
        x = num % 10
        if x % 2 == 0 and x != 0:
            cont += 1
        num = num // 10
    return True if cont >= 2 else False

def ingresar():
    n = int(input("Ingrese numero: "))
    while not dosPares(n):
        n = int(input("No cumple, ingrese otro numero: "))
    return n

def main():
    print("El numero {} contiene aunque sea 2 digitos pares.".format(ingresar()))
main()
