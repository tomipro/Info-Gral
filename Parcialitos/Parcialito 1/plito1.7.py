from math import pi
def areaCuad(lado):
    areaCuad=(lado**2)
    return areaCuad
def areaCirc(radio):
    areaCirc=(pi)*(radio**2)
    return areaCirc
def areaTriag(b,a):
    areaTriag=(0.5)*(b*a)
    return areaTriag
def areaNegra(x):
    areaNegra=(2*(areaCuad(x)))+(2*(areaTriag((x/2),(x))))+(areaCirc(x/4))-(2*(areaCirc(x/2)))
    return areaNegra
def areaBlanca(x):
    areaBlanca=(2*(areaCirc(x/2)))-(areaCirc(x/4))-(2*(areaTriag((x/2),(x))))
    return areaBlanca
def main():
    x=int(input("Ingrese valor X: "))
    AN=areaNegra(x)
    AB=areaBlanca(x)
    AT=AN+AB
    ANpor=(AN/AT)*100
    ABpor=(AB/AT)*100
    print("\n@ Porc. AN: {:.2f}% @ El AN es: {:.2f}\n\n@ Porc. AB: {:.2f}% @ El AB es: {:.2f}\n\nEl area TOTAL es: {:.2f}".format(ANpor,AN,ABpor,AB,AT))
main()