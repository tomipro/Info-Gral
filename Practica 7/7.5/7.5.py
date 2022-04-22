from typing import NoReturn

def esLetra(c: str) -> bool:
    return True if ((c >= "a" and c <= "z") or (c >= "A" and c <= "Z") or (c in "áéíóúÁÉÍÓÚ")) else False

def cabecera2(arch: str, cant: int, pmin: int, pmax: int) -> NoReturn:
    archivo = open(arch, "r")
    texto = ""
    for linea in archivo:
        texto += linea
    archivo.close()
    total = 0
    i = 0
    lst = []
    while i < len(texto):
        while i < len(texto) and not esLetra(texto[i]):
            i += 1
        palabra = ""
        while i < len(texto) and esLetra(texto[i]):
            palabra += texto[i]
            i += 1
        if palabra and palabra not in lst and (pmax >= len(palabra) >= pmin) and total < cant:
            total += 1
            lst.append(palabra)
    final = ""
    for pal in lst:
        final += pal + "\n"
    archivoSalida = open("/Users/tomasprodan/Documents/Info GRAL/Practica 7/7.5/output7.5.csv", "w")
    archivoSalida.write(final)
    archivoSalida.close()

def main():
    arch = "/Users/tomasprodan/Documents/Info GRAL/Practica 7/7.3.2/7.3.2.txt"
    cant = int(input("Ingrese cantidad: "))
    pmin = int(input("Ingrese pmin: "))
    pmax = int(input("Ingrese pmax: "))
    cabecera2(arch, cant, pmin, pmax)
main()
