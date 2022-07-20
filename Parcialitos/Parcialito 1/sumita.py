import math
def primCif(num):
    digitos=int(math.log10(num))
    num=int(num/pow(10,digitos))
    return num
def sumita(n1,n2):
    numero1=primCif(n1)
    numero2=primCif(n2)
    return numero1+numero2
def main():
    n1=int(input("Ingrese primer numero: "))
    n2=int(input("Ingrese segundo numero: "))
    print(sumita(n1,n2))
main()