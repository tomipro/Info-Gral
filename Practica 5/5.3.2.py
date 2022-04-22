def esPalabra(pal):
    x=0
    for car in pal:
        if (car>="A" and car<="Z") or (car>="a" and car<="z"):
            x+=1
    return True if x==len(pal) else False

def esPar(pal):
    return True if (len(pal)%2==0) else False

def fun(pal):
    bandera=False
    while not bandera:
        if (esPar(pal) and esPalabra(pal)):
            pal=input("Ingrese palabra de longitud par: ")
            bandera=True
        else:
            pal=input("Error. Ingrese palabra de longitud par: ")
    return pal[:((len(pal))//2)]

# def fun(pal):
#     pal=ingreso(pal)
#     return 

def main():

main()

#como validar en otra funcion para no hacerlo dentro del main?