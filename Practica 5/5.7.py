def caps(fra):
    x=""
    i=0
    while i<len(fra):
        if fra[i]>="a" and fra[i]<="z":
            x+=chr(ord(fra[i])-32)
        else:
            x+=fra[i]
        i+=1
    return x

def contar(larga,corta):
    res=0
    cortaLong=len(corta)
    if cortaLong!="":
        for i in range(len(larga)):
            if caps(larga)[i:i+cortaLong]==caps(corta):
                res+=1
    else:
        res=1
    return res

def main():
    l=input("Ingrese el texto largo: ")
    c=input("Ingrese el texto corto: ")
    while c=="":
        c=input("Error. Ingrese el texto corto: ")
    print("El texto corto se encontró {} veces en el texto largo".format(contar(l,c))) if contar(l,c)>0 else print("No aparece nunca")
main()