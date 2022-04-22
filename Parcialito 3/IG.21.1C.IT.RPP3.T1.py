def esLetra(car):
    return True if ((car >= "a" and car <= "z") or (car >= "A" and car <= "Z")) else False

def caps(txt):
    i = 0
    temp = ""
    while i < len(txt):
        if txt[i] >= "a" and txt[i] <= "z":
            temp += chr(ord(txt[i]) - 32)
        else:
            temp += txt[i]
        i += 1
    return temp

def fun(txt):
    i = 0
    lst = []
    while i < len(txt):
        while i < len(txt) and not esLetra(txt[i]):
            i += 1
        pal = ""
        bandera = False
        while i < len(txt) and esLetra(txt[i]):
            bandera = True
            pal += txt[i]
            i += 1
        if bandera and pal not in lst and "BILIDAD" in pal:
            lst.append(caps(pal))
    return lst

def main():
    texto = "gracias por su amabilidad, su Santidad tiene la habilidad de transmitir estabilidad con amabilidad."
    texto = caps(texto)
    res = fun(texto)
    print(res)
main()