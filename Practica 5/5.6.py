def esLetra(car):
    return True if ((car>="a" and car<="z") or (car>="A" and car<="Z")) else False
#áéíóúÁÉÍÓÚ
def caps(texto):
    i = 0
    temp = ""
    while i<len(texto):
        if texto[i]>="a" and texto[i]<="z":
            temp+=chr(ord(texto[i])-32)
        else:
            temp+=texto[i]
        i+=1
    return temp

def fun(texto):
    i = 0
    temp = ""
    while i<len(texto):
        while i<len(texto) and not esLetra(texto[i]):
            i+=1
        while i<len(texto) and esLetra(texto[i]):
            temp+=texto[i]
            i+=1
    return caps(temp)

def invertir(texto):
    return (fun(texto))[::-1]

def comparar(texto):
    print("La frase es palindroma!") if fun(texto)==invertir(texto) else print("La frase NO es palidroma!")

def main():
    texto=input("Ingrese una frase: ")
    comparar(texto)
main()
#í?
#print(invertir("Asi Ramona va, no Marisa"))