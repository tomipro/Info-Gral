import math
def subnumero(num,limSup,limInf):
    num=num//pow(10,limInf-1)
    num=num%pow(10,limSup)
    return int(num)
def main():
    num=int(input("Ingrese numero: "))
    limSup=int(input("Ingrese limite superior: "))
    limInf=int(input("Ingrese limite inferior: "))
    print(subnumero(num,limSup,limInf))
main()