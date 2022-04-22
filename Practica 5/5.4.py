def esLetra(car):
    return True if ((car>="a" and car<="z") or (car>="A" and car<="Z")) else False

def primeraPalabra(texto):
    i=0
    temp=""
    while i<len(texto) and not esLetra(texto[i]):
        i+=1
    while i<len(texto) and esLetra(texto[i]):
        temp+=texto[i]
        i+=1
    return temp

def ultimaPalabra(texto):
    i=-1
    temp=""
    while i>=(-len(texto)) and not esLetra(texto[i]):
        i-=1
    while i>=(-len(texto)) and esLetra(texto[i]):
        temp=texto[i]+temp
        i-=1
    return temp

def caps(texto):
    i=0
    temp=""
    while i<len(texto):
        if texto[i]>="a" and texto[i]<="z":
            temp+=chr(ord(texto[i])-32)
        else:
            temp+=texto[i]
        i+=1
    return temp

def principioFin(texto):
    return True if caps(ultimaPalabra(texto))==caps(primeraPalabra(texto)) else False

def main():
    texto=input("Ingrese un texto: ")
    print("El texto cumple la condicion.") if principioFin(texto) else print("El texto NO cumple la condicion.")
main()