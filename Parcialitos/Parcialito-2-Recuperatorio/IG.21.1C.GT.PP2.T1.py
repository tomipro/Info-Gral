def reloj(num):
    for i in range(num):
        for j in range(num):
            if ((i==0) or (i == j) or (i + j == num - 1) or (i>=j and j >= num//2) or (i+j>=num-1 and j<=num//2)):
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print()

def main():
    num = int(input("Ingrese N: "))
    while num % 2 == 0 or num < 7:
        num = int(input("Error. Ingrese N: "))
    reloj(num)
main()