def extrem(pal,car):
    if len(car)!=2 or pal=="":
        return "\nLa funcion ha retornado una palabra vacia"
    elif len(car)==2:
        nPal=car[0]+pal+car[1]
        return nPal
def main():
    car=input("Ingrese los extremos: ")
    pal=input("Ingrese la palabra: ")
    print("\nLa funcion retorno: {}".format(extrem(pal,car)))
main()