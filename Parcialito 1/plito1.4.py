from math import pi
def areaCuad(lado):
    areaCuad=(lado**2)
    return areaCuad
def areaCirc(radio):
    areaCirc=(pi)*(radio**2)
    return areaCirc
def areaTriag(base,altura):
    areaTriag=(0.5)*(base*altura)
    return areaTriag
def areaNegra(x):
    areaNegra=((3)*(areaCuad(x/2)))-(areaTriag((x/2),(x/2)))
    return areaNegra
def areaBlanca(x):
    areaBlanca=((areaCuad(x/2))+(areaTriag((x/2),(x/2))))
    return areaBlanca
def main():
    x=int(input("Ingrese valor X: "))
    AN=areaNegra(x)
    AB=areaBlanca(x)
    AT=AN+AB
    ANpor=(AN/AT)*100
    ABpor=(AB/AT)*100
    print("\nEl area TOTAL es: {:.2f}\n________________________________________\nEl AN es: {:.2f} | Porc. AN: {:.2f}%\nEl AB es: {:.2f} | Porc. AB: {:.2f}\n________________________________________".format(AT,AN,ANpor,AB,ABpor))
main()