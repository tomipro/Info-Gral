def dibujar(n):
    for i in range(n):
        for j in range(n):
            if (i==0 or j==0 or i==n-1 or j==n-1 or i==j or (j>=n//2) and i<=(n-1)//2):
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