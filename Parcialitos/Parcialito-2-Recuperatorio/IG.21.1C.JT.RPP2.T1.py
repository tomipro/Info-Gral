from random import randint as ri
def condicion(num):
    suma = 0
    i = 0
    while num > 0:
        digitos = num % 10
        suma += digitos
        i += 1
        num = num // 10
    return (suma / i) < 5

def funcion(a, b):
    num = ri(a, b)
    while not condicion(num):
        num = ri(a,b)
    return num

def main():
    a = int(input("Ingrese primer valor: "))
    while not a > 0:
        a = int(input("Error. Ingrese primer valor: "))
    b = int(input("Ingrese segundo valor: "))
    while not a < b:
        b = int(input("Error. Ingrese segundo valor: "))
    print("Resultado: {}".format(funcion(a, b)))
main()