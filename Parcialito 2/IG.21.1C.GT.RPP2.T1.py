# def dosPares(n):
#     i=0
#     while n>0:
#         digitos=n%10
#         if digitos%2==0:
#             i+=1
#         n=n//10
#     if i>=2:
#         return True
#     else:
#         return False
# def ingresar():
#     num=int(input("Ingrese numero entero: "))
#     while not dosPares(num):
#         num=int(input("Ingrese numero entero: "))
#     return num
# def main():
#     x=ingresar()
#     print("El valor {} tiene dos o mas digitos pares.".format(x))
# main()
# def dosPares(n):
#     i=0
#     while n>0:
#         dig=n%10
#         if dig%2==0:
#             i+=1
#         n=n//10
#     if i>=2:
#         return True
#     else:
#         return False
# def ingresar():
#     x=int(input("Ingrese numero: "))
#     while not dosPares(x):
#         x=int(input("Ingrese numero: "))
#     print("Cumple")
# ingresar()

def dosPares(n):
    i=0
    while n>0:
        dig=n%10
        if dig%2==0 and dig!=0:
            i+=1
        n=n//10
    if i>=2:
        return True
    else:
        return False
def ingresar():
    num=int(input("Ingrese numero: "))
    while not dosPares(num)==True:
        num=int(input("Ingrese numero: "))
    print("Cumple")
ingresar()