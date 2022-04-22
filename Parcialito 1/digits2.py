import math
def sumita(n1,n2):
    n1=primCif(n1)
    n2=primCif(n2)
    return n1+n2

def primCif(num):
    digitos=int(math.log10(num))
    num=int(num/pow(10,digitos))
    return num

def main():
    n1=int(input("Ingrese primer numero: "))
    suma=sumita(n1)
main()