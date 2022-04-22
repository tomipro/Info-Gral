def funcion(num):
    i=0
    while i<5:
        if num%2==0:
            i+=1
            if num%4==0:
                print(f"Numero par. Tambien es multiplo de 4. Cantidad de numeros pares: {i}")
            else:
                print(f"Numero par. Cantidad de numeros pares: {i}")
        if i<5:
            num=int(input("Ingrese numero: "))
    print("\nFIN.")
def main():
    num=int(input("Ingrese numero: "))
    funcion(num)
main()