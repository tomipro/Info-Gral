def esLetra(car):
    return True if ((car >= "a" and car <= "z") or (car >= "A" and car <= "Z")) else False

def fun(txt):
    lst = []
    i = 0
    while i < len(txt):
        while i < len(txt) and not esLetra(txt[i]):
            i += 1
        pal = ""
        bandera = False
        while i < len(txt) and esLetra(txt[i]):
            bandera = True
            pal += txt[i]
            i += 1
        if bandera and pal not in lst:
            lst.append(pal)
    return lst

def main():
    texto = input("Ingrese frase: ")
    print(fun(texto))
main()