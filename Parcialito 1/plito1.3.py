from math import pi
def areaCuad(lado):
    areaCuad=(lado**2)
    return areaCuad
def areaCirc(radio):
    areaCirc=(pi)*(radio**2)
    return areaCirc
def areaTriag(b,a):
    areaTriag=((0.5)*(b*a))
    return areaTriag
def areaNegra(x):
    areaNegra=((areaCuad(x/2)))+(areaCuad(x))-(areaTriag((x/2),(x/2)))-(areaCirc((x/4))*(3/2))
    return areaNegra
def areaBlanca(x):
    areaBlanca=(areaTriag((x/2),(x/2)))+((3)*(areaCirc(x/4)))
    return areaBlanca
def main():
    x=int(input("Ingrese valor X: "))
    AN=areaNegra(x)
    AB=areaBlanca(x)
    AT=AN+AB
    ANpor=(AN/AT)*100
    ABpor=(AB/AT)*100
    print("\nEl AN es: {:.2f} y su Porc. es AN: {:.2f}%\nEl AB es: {:.2f} y su Porc. es AB: {:.2f}%\nEl area TOTAL es: {:.2f}".format(AN,ANpor,AB,ABpor,AT))
main()