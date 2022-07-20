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
    areaNegra=(2*(areaCuad(x/2))+(0.5*(areaCirc(x/2))))
    return areaNegra
def areaBlanca(x):
    areaBlanca=(0.5*areaCirc(x/2))
    return areaBlanca
def main():
    x=int(input("Ingrese lado: "))
    AN=areaNegra(x)
    AB=areaBlanca(x)
    AT=AN+AB
    ANpor=(AN/AT)*100
    ABpor=(AB/AT)*100
    print("AN= {:.2f} ANpor= {:.2f}%\nAB= {:.2f} ABpor= {:.2f}%\nAT= {:.2f}".format(AN,ANpor,AB,ABpor,AT))
main()