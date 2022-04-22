def escribirArch():
    print("----------escribirArch()---------------")
    import random
    arch = open("/Users/tomasprodan/Documents/Info GRAL/Practica 7/Teoria 09-11-21/archLec.txt","a")
    a = random.randint(0, 99)
    b = random.randint(0, 99)
    c = random.randint(0, 99)

    contenido = "23, 5, 9\n34, 78, 9\n"
    contenido += str(a) + ", " + str(b) + ", " + str(c) + "\n"

    arch.write(contenido)
    arch.write("0, 0, 0\n")
    arch.write("**********\n")
    
    arch.close()
    print("----se escribió el archivo archEsc.txt--")
escribirArch()