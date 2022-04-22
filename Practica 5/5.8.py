def esLetra(car):
    return True if ((car>="a" and car<="z") or (car>="A" and car<="Z")) else False
def mayus(car):
    return chr(ord(car)-32)
def fun(frase):
    i=0
    res=""
    x=False
    while i<len(frase):
        while i<len(frase) and not esLetra(frase[i]):
            res+=frase[i]
            i+=1
        x=True
        while i<len(frase) and esLetra(frase[i]):
            if x==True:
                res+=mayus(frase[i])
                x=False
            else:
                res+=frase[i]
            i+=1
    return res
def main():
    texto=input("Ingrese un texto: ")
    print("La funcion ha retornado:"+fun(texto))
main()