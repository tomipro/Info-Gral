import math
def promedio(num1,num2,num3):
    prom=(num1+num2+num3)/3
    return prom
def imprimirPromedioFormateado(prom):
    print("\nPromedio:{:>30}".format(prom))
def main():
    num=int(input("Ingrese numero de 5 digitos: "))
    digs=int(math.log10(num))
    num1=int(num/pow(10,digs))
    num2=int(num/pow(10,(digs/2))%10)
    num3=num%10
    prom=promedio(num1,num2,num3)
    imprimirPromedioFormateado(prom)
main()