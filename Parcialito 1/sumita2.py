import math
def primCif(num):
    digitos=int(math.log10(num))
    num=int(num/pow(10,digitos))
    return num
def sumita(n1,n2):
    n1=primCif(n1)
    n2=primCif(n2)
    sumita=n1+n2
    return sumita
def main():
    num1=int(input("Ingrese primer numero: "))
    num2=int(input("Ingrese segundo numero: "))
    primero1=primCif(num1)
    primero2=primCif(num2)
    sum=sumita(num1,num2)
    print("Ejemplo:\n\nEl llamado a Primcif con parametro: {} retorna {}\n\nEl llamado a Primcif con parametro {} retorna {}\n\nEl llamado a Sumita con parametros {} y {} retorna {}\n".format(num1,primero1,num2,primero2,num1,num2,sum))
main()