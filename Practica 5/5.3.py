def esLetra(car):
    return True if ((car>="a" and car<="z") or (car>="A" and car<="Z")) else False

def esPar(pal):
    return True if (len(pal)%2==0) else False

def fun(pal):
    i=0
    if (i<len(pal) and esLetra(pal[i])):
        while not esPar(pal):
            pal=input("Error. Ingrese palabra de longitud par: ")
            fun2(pal)
    

def fun2(pal):
    i=0
    while i<len(pal) and esLetra(pal[i]):
        lenpal=0
        i+=1
        lenpal=i
    return lenpal

def ingreso(pal):
    pal=input("Ingrese palabra de longitud par: ")
    while not esPar(pal) or :
        pal=input("Error. Ingrese una palabra de longitud par: ")

def main():
    pal=input("Ingrese palabra de longitud par: ")
    print(fun(pal))
main()

