# from random import randint as r
# def fun(n):
#     suma=0
#     i=0
#     while n>0:
#         cantDig=n%10
#         suma+=cantDig
#         i+=1
#         n=n//10
#     return suma/i<5
# def buscar(a,b):
#     num=r(a,b)
#     while not fun(num):
#         num=r(a,b)
#     return num
# def main():
#     a=int(input("Ingrese primer numero: "))
#     while a<0:
#         a=int(input("Error. Ingrese primer numero: "))
#     b=int(input("Ingrese segundo numero: "))
#     while b<=a:
#         b=int(input("Error. Ingrese segundo numero: "))
#     print("Resultado:",buscar(a,b))
# main()
from random import randint as ri
def fun(n):
    suma=0
    i=0
    while (n>0):
        digitos=n%10
        suma+=digitos
        i+=1
        n=n//10
    return (suma/i)<5
def buscar(a,b):
    num=ri(a,b)
    while not fun(num):
        num=ri(a,b)
    return num
def main():
    a=int(input("Ingrese primer numero: "))
    while (a<0):
        a=int(input("Error. Ingrese primer numero: "))
    b=int(input("Ingrese segundo numero: "))
    while (b<=a):
        b=int(input("Error. Ingrese segundo numero: "))
    resultado=buscar(a,b)
    print("Valor generador con suma menor a 5 dentro de intervalo ({}, {}) es: {}".format(a,b,resultado))
main()