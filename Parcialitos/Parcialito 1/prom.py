import math
def promedio(n1,n2,n3):
    prom=(n1+n2+n3)/3
    return prom
def imprimirPromedioFormateado(prom):
    print("Promedio:{:>30}".format(prom))
def main():
    num=int(input("Ingrese numero de 5 digitos: "))
    digitos=int(math.log10(num))
    n1=int(num/pow(10,digitos))
    n2=int(num/pow(10,(digitos/2))%10)
    n3=num%10
    prom=promedio(n1,n2,n3)
    imprimirPromedioFormateado(prom)
main()