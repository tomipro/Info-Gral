# # import math as m
# # def cifras(num):
# #     digs=int(m.log10(num))
# #     prim=int((num//(m.pow(10,digs))))
# #     ult=num%10
# #     return prim, ult
# # def sumatoria(n):
# #     prim,ult=cifras(n)
# #     suma=0
# #     if n>0:
# #         for a in range(prim+1,ult):
# #             suma+=a
# #         return suma
# # def multiplicacion(n):
# #     prim,ult=cifras(n)
# #     while n>=10:
# #         mult=prim*ult
# #     return mult
# # def validarT1(numero):
# #     if multiplicacion(numero)==sumatoria(numero):
# #         return "True"
# #     else:
# #         return False
# # def main():
# #     numero=int(input("Ingrese numero: "))
# #     validarT1(numero)
# # main()
# import math
# def digitos(num):
#     digs=int(math.log10(num))
#     prim=int(num/(math.pow(10,digs)))
#     ult=num%10
#     return digs, prim, ult
# def producto(num):
#     digs,prim,ult=digitos(num)
#     prod=prim*ult
#     return prod
# def sumatoria(num):
#     digs,prim,ult=digitos(num)
#     centrales=num%(10**(digs))
#     centrales=centrales//10
#     suma=0
#     dig=centrales%10
#     while num!=0:
#         suma+=dig
#         num=num//10
#         dig=num%10
#     return suma
    
# # def validarT1(num):
# #     if (sumatoria(num)==producto(num)):
# #         return True
# #     else:
# #         return False
# def main():
#     x=int(input("Ingrese numero: "))
#     # print(validarT1(x))
#     print(sumatoria(x))
#     print(producto(x))
#     print(digitos(x))
# main()


def largoNum(num):
    lar=0
    while num>0:
        lar+=1
        num=num//10
    return lar
def suma(num):
    largo=largoNum(num)
    centrales=num%(10**(largo-1))
    dig=centrales%10
    suma=0
    while num!=0:
        suma+=dig
        num=num//10
        dig=num%10
    return suma

def producto(num):
    largo=largoNum(num)
    izq=num//(10**(largo-1))
    der=num%10
    mult=izq*der
    return mult

def validarT1(num):
    if (suma(num)==producto(num)):
        return True
    else:
        return False
def main():
    x=int(input("Ingrese numero: "))
    print(validarT1(x))
    print(suma(x))
    print(producto(x))
    print(largoNum(x))
main()