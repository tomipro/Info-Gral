def rotacion(frase):
    fra1=frase[(len(frase)//2):]
    fra2=frase[:(len(frase)//2)]
    return fra1+fra2
def main():
    frase=input("Ingrese un texto: ")
    while (len(frase)<=2 or len(frase)%2!=0):
        frase=input("Error. Ingrese un texto: ")
    print("La funcion ha retornado: {}".format(rotacion(frase)))
main()