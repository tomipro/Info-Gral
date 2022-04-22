from typing import NoReturn

def esLetra(c: str) -> bool:
    return True if ((c >= "a" and c <= "z") or (c >= "A" and c <= "Z") or c in "áéíóúÁÉÍÓÚ") else False

def cabecera(arch: str, cant: int, pmax: int, pmin:int) -> NoReturn:
    archivo = open(arch, "r")
    texto = ""
    for linea in archivo:
        texto += linea
    archivo.close()
    tot = 0
    i = 0
    while i < len(texto):
        while i < len(texto) and not esLetra(texto[i]):
            i += 1
        palabra = ""
        while i < len(texto) and esLetra(texto[i]):
            palabra += texto[i]
            i += 1
        if palabra and len(palabra) >= pmin and len(palabra) <= pmax and tot < cant:
            tot += 1
            print(palabra)

def main():
    arch = "/Users/tomasprodan/Documents/Info GRAL/Practica 7/7.3.2/7.3.2.txt"
    cant = int(input("Ingrese cantidad: "))
    pmax = int(input("Ingrese pmax: "))
    pmin = int(input("Ingrese pmin: "))
    cabecera(arch, cant, pmax, pmin)
main()
