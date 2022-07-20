def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        a=0
        b=1
        for i in range(3,n+1):
            fibonacci=a+b
            a=b
            b=fibonacci
        return fibonacci
# def fib(n):
#     if n==1:
#         fibo=0
#     elif n==2:
#         fibo=1
#     else:
#         a=0
#         b=1
#         i=3
#         while i<=n:
#             fibo=a+b
#             a=b
#             b=fibo
#             i+=1
#     return fibo
def main():
    num=int(input("Ingrese un numero natural menor que 20: "))
    while num>=20 or num<=0:
        num=int(input("Error! Ingrese un numero natural menor que 20: "))
    fibon=fib(num)
    print("El termino {} de la serie de Fibonacci es: {}".format(num,fibon))
main()