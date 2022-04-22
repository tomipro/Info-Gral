import math
def subnumero(num,lim_sup,lim_inf):
    num=num//math.pow(10,lim_inf-1)
    num=num%math.pow(10,lim_sup)
    return int(num)
def main():
    lim_sup=int(input("Ingrese limite superior: "))
    lim_inf=int(input("Ingrese limite inferior: "))
    num=int(input("Ingrese numero: "))
    print(subnumero(num,lim_sup,lim_inf))
main()