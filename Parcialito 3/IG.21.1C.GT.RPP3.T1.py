def esLetra(car):
    return True if (car >= "a" and car <= "z") or (car >= "A" and car <= "Z") else False

def esVocal(car):
    return True if (car in "aeiouAEIOU") else False

def listita(txt):
    i = 0
    lst = []
    while i < len(txt):
        while i < len(txt) and not esLetra(txt[i]):
            i += 1
        pal = ""
        cont = 0
        while i < len(txt) and esLetra(txt[i]):
            if esVocal(txt[i]):
                cont += 1
            pal += txt[i]
            i += 1
        if cont > 3:
            lst.append(pal)
    return lst

def main():
    texto = "..., Otto Orozco y Hans Orozco--, quisieran rodar sus maquinas! Vamos hombres!!!!!"
    res = listita(texto)
    print(res)
main()