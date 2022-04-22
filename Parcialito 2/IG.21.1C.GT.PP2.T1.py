# def reloj(num):
#     for i in range(num):
#         for j in range(num):
#             if(
#                 i==0 or i==j or i+j==(num-1) or (i>j and i+j>num-1)
#             ):
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         print()
# def main():
#     num=int(input("num = "))
#     while num%2==0 or num<=7:
#         num=int(input("num = "))
#     reloj(num)
# main()

def reloj(num):
    for i in range(num):
        for j in range(num):
            if (
                i==0 or i==j or i+j==num-1 or
                (i+j>=num-1 and i<=j) or (i+j<=num-1 and i>=j) or i==num-1
            ):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def main():
    num=int(input("Ingrese numero: "))
    while num%2==0 or num<7:
        num=int(input("Error. Ingrese numero: "))
    reloj(num)
main()