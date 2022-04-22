def dibujar(n):
    for i in range(n):
        for j in range(n):
            if (i==n-1 or j==n-1 or i==j or i+j==n-1 or (i+j<=(n-1)//2)):
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print()

def main():
    n = int(input("Ingrese N: "))
    while n % 2 != 0 or n < 6:
        n = int(input("Error, ingrese N: "))
    dibujar(n)
main()
