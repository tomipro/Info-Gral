def figura(n):
    for i in range(n):
        for j in range(n):
            if (
                j == n // 2 or (i == 0 and j >= (n // 2)) or (j == (n - 1) and i <= (n // 2))
                or (i-j==-(n-1)//2) or (i-j>=n//2)
            ):
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print()

def main():
    n = int(input("Ingrese altura (impar): "))
    while not n % 2 !=0:
        n = int(input("Error. Ingrese altura (impar): "))
    figura(n)
main()