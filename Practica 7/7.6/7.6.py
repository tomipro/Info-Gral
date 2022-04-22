from typing import NoReturn
import random
import time

def esLetra(car: str) -> bool:
    return True if ((car >= "a" and car <= "z") or (car>= "A" and car <= "Z") or car in "áéíóúÁÉÍÓÚ") else False

def generadora(ori: str, dest: str, cant: int) -> NoReturn:
    archivo = open(ori, "r")
    texto = ""
    for linea in archivo:
        texto += linea
    archivo.close()
    i = 0
    lst = []
    while i < len(texto):
        while i < len(texto) and not esLetra(texto[i]):
            i += 1
        palabra = ""
        while i < len(texto) and esLetra(texto[i]):
            palabra += texto[i]
            i += 1
        if palabra and palabra not in lst:
            lst.append(palabra)
    lstAux = []
    for j in range(len(lst)):
        k = random.randint(0, len(lst) - 1)
        elemento = lst.pop(k)
        if len(lstAux) < cant:
            lstAux.append(elemento)
    textoAleatorio = ""
    i = 0
    for pal in lstAux:
        textoAleatorio += pal + "\n"
        i += 1
        print(f"{i:<3} - {pal:>20}")
        time.sleep(0.1)
    archivoDestino = open(dest, "w")
    archivoDestino.write(textoAleatorio)
    archivoDestino.close()
    

def main():
    arch = "/Users/tomasprodan/Documents/Info GRAL/Practica 7/7.3.2/7.3.2.txt"
    dest = "/Users/tomasprodan/Documents/Info GRAL/Practica 7/7.6/7.6destino.txt"
    cant = int(input("Ingrese cantidad: "))
    generadora(arch, dest, cant)
main()
