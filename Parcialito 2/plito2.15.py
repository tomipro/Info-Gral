def dibujar(n):
    for i in range(n):
        for j in range(n):
            if (
                j==(n-1)/2 or (i-j==-(n-1)/2) or (i==0 and j>(n-1)/2) or (j==n-1 and i<(n-1)/2)
                or (i-j>=(n-1)/2  )
            ):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def main():
    n=int(input("Ingrese numero: "))
    while n%2==0 or n<5:
        n=int(input("Error. Ingrese numero: "))
    dibujar(n)
main()