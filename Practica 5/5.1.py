def copiar(pal):
    if len(pal)<2:
        return "La funcion ha retornado una palabra vacia"
    else:
        return pal[-2:]*3
def main():
    pal=input("Ingrese una palabra: ")
    print(copiar(pal))
main()