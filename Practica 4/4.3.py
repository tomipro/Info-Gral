def esPrimo(num):
    lst = []
    if num > 1:
        for i in range(2, int(num**0.5)+1):
            if num % i != 0:
                lst.append(i)
    print(lst)
    # return lst

def fun(num):
    lst = []
    i = 2
    while i < num:
        if num % i == 0:
            lst.append(i)
        i += 1
    print(lst)
    

# def fun(num):
#     lst = esPrimo(num)
#     print("Primos entre 1 y {}:".format(num))
#     for i in range(1, len(lst)):
#         if i in lst:
#             print("{:6}".format(i))

# def fun2(num):
#     lst = esPrimo(num)
#     n = 0
#     print("\nPrimeros {} primos:\n".format(num))
#     for i in range(1, n):
#         if n % i == 0:
#             print("{:6}".format(n))
#         n += 1

def main():
    num = int(input("Ingrese cantidad (numero natural): "))
    # esPrimo(num)
    fun(num)
    # fun2(num)
main()
