def dibujar(n):
    for i in range(n):
        for j in range(n):
            if i==0 or j==0 or i==n-1 or j==n-1 or (i<((n-1)/2) and j>((n-1)/2)) or (i>((n-1)/2) and j<((n-1)/2)):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def main():
    n=int(input("Ingrese numero: "))
    while n%2!=0 or n<6:
        n=int(input("Error. Ingrese numero: "))
    dibujar(n)
main()