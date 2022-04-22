def main():
    arch = open("archivo.txt", "r")
    lstArch = arch.readlines()
    print(lstArch)
    arch.close()
main()