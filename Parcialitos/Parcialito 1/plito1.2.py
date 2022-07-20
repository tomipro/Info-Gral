import math
def areaCua(c):
    areaCua=(c**2)
    return areaCua
def areaCir(r):
    areaCir=(math.pi)*(r**2)
    return areaCir
def areaNegra(c):
    areaNegra=(areaCua(c))-(areaCir(c/2))+(areaCir(c/4))
    return areaNegra
def main():
    lado=int(input("Ingrese lado: "))
    print("La superficie gris es",areaNegra(lado))
main()