def main():
    arch = open("/Users/tomasprodan/Documents/Info GRAL/Practica 7/Teoria 09-11-21/ej1/archivo.txt", "r")
    lstArch = arch.readlines()
    print(lstArch)
    arch.close()
main()