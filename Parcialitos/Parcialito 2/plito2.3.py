# def dibujar(n):
#     for i in range(n):
#         for j in range(n):
#             if j==0 or (i==n-1 and j>(n/2)-1) or j==n-1 or (i==j and j<(n/2)-1) or i+j==n-1 or (i+j>n-1 and (j>n/2 and i<n/2)):
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         print()
# def main():
#     n=int(input("Ingrese numero impar: "))
#     while n%2==0 or n<5:
#         n=int(input("Error. Ingrese numero impar mayor a 5: "))
#     dibujar(n)
# main()
# def dibujar(n):
#     for i in range(n):
#         for j in range(n):
#             if (
#                 j==0 or (i==n-1 and j>n//2) or j==n-1 or (i+j>n-1 and i<=n//2)
#                 or i+j==n-1 or (i==j and j<n//2)
#             ):
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         print()
# def main():
#     n=int(input("Ingrese numero: "))
#     while n%2==0 or n<5:
#         n=int(input("Error. Ingrese numero: "))
#     dibujar(n)
# main()

def dibujar(n):
    for i in range(n):
        for j in range(n):
            if (j==0 or j==n-1 or (i==j and j<n//2) or i+j==n-1 or (i==n-1 and j>=n//2)
            or (i+j>n-1 and i<=n//2)
            ):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def main():
    n=int(input("Ingrese numero: "))
    while n%2==0 or n<7:
        n=int(input("Error. Ingrese numero: "))
    dibujar(n)
main()