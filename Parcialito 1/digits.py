import math
def main():
    num=int(input("Ingrese numero: "))
    digits=int(math.log10(num))+1
    digits2=num%10
    print(digits)
    print(digits2)
main()