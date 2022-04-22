def funcion(num):
    i=mayor=menor=0
    while num!=0:
        if i==0:
            mayor=num
            menor=num
            i+=1
        if num>mayor:
            mayor=num
        if num<menor:
            menor=num
        num=int(input())
        while num<0:
            num=int(input("Error. Ingrese numero:" ))
    if i!=0:
        print("El mayor es {} y el menor es {}".format(mayor,menor))
def main():
    num=int(input("Ingrese numero: "))
    funcion(num)
main()