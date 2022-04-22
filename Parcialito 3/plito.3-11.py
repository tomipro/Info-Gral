def esLetra(car):
    return True if ((car >= "a" and car <= "z") or (car >= "A" and car <= "Z")) else False

def caps(txt):
    i = 0
    temp = ""
    while i < len(txt):
        if txt[i] >= "a" and txt[i] <="z":
            temp += chr(ord(txt[i]) - 32)
        else:
            temp += txt[i]
        i += 1
    return temp

def lista_pal(fra, lst):
    i = 0
    while i < len(fra):
        while i < len(fra) and not esLetra(fra[i]):
            i += 1
        pal = ""
        bandera = False
        while i < len(fra) and esLetra(fra[i]):
            bandera = True
            pal += fra[i]
            i += 1
        if bandera and pal not in lst:
            lst.append(caps(pal))
    return lst

def eliminar_repetidas(lst):
    lista = []
    for i in lst:
        if i not in lista:
            lista.append(i)
    return lista

def main():
    frase = "Hombre de poca fe, he dicho! Vamos, --vamos--, si VAMOS hombre!!!"
    lista = []
    print(lista_pal(frase, lista))
    print(eliminar_repetidas(lista))
main()






"""
def aMayus(txt):
    i = 0
    temp = ""
    while i < len(txt):
        if txt[i] >= "a" and txt[i] <= "z":
            temp += chr(ord(txt[i]) - 32)
        else:
            temp += txt[i]
        i += 1
    return temp

def lista_pal(fra, lst):
    i = 0
    while i < len(fra):
        while i < len(fra) and not esLetra(fra[i]):
            i += 1
        pal = ""
        bandera = False
        while i < len(fra) and esLetra(fra[i]):
            bandera = True
            pal += fra[i]
            i += 1
        if bandera:
            lst.append(aMayus(pal))
    return lst
    """