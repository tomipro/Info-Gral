import math
def areaRec(b):
    areaRec=(2*b)*(b)
    return areaRec
def areaCir(r):
    areaCir=(math.pi)*(r**2)
    return areaCir
def areaTri(b):
    areaTri=(0.5)*(b**2)
    return areaTri
def areaNegra(b):
    areaNegra=(areaRec(b))-(areaTri(b))-(areaCir(b/2))
    return areaNegra
def main():
    lado=int(input("Ingrese la base: "))
    print("La superf. negra es:",areaNegra(lado))
main()