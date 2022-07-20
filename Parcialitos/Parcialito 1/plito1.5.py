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
    areaNegra=(0.5*(areaCirc(x/2)))+(areaCuad(x/4))
    return areaNegra
def areaBlanca(x):
    areaBlanca=(0.5*areaCirc(x/2))-(areaCuad(x/4))
    return areaBlanca
def main():
    x=int(input("Ingrese valor X: "))
    AN=areaNegra(x)
    AB=areaBlanca(x)
    AT=AN+AB
    ANpor=(AN/AT)*100
    ABpor=(AB/AT)*100
    print(f"El AN es: {AN:.2f} | Porc. AN: {ANpor:.2f}%\nEl AB es: {AB:.2f} | Porc. AB: {ABpor:.2f}%\n\nEl area TOTAL es: {AT:.2f}")
main()