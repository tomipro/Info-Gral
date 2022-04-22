def esLetra(car):
    return True if ((car >= "a" and car <= "z") or (car >= "A" and car <= "Z")) else False

def obtener_palabras(s):
    i = 0
    lst = []
    while i < len(s):
        while i < len(s) and not esLetra(s[i]):
            i += 1
        pal = ""
        while i < len(s) and esLetra(s[i]):
            pal += s[i]
            i += 1
        lst.append(pal)
    return lst

def procesar(s1, s2):
    # lista = []
    l1 = obtener_palabras(s1)
    l2 = obtener_palabras(s2)
    return list(set(i for i in l1 if not i in l2))
    # for i in l1:
    #     if i not in l2:
    #         if i not in lista:
    #             lista.append(l1)
    # return lista

def main():
    frase1 = "luis, con su nuevo uniforme, se pavonea orgullosamente con su amigo"
    frase2 = "luis se ha lustrado los zapatos para lucir su nuevo uniforme"
    lista = procesar(frase1, frase2)
    print(lista)
main()
#se imprime ['con', 'pavonea', 'orgullosamente', 'amigo']