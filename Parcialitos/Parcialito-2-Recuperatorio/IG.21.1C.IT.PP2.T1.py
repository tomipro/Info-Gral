# from functools import cache

# @cache
# def fib(n):
#     return n if n <= 1 else (fib(n-1) + fib(n-2))
def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        a = 0
        b = 1
        for i in range(3, n+1):
            fib = a + b
            a = b
            b = fib
        return fib

def main():
    n = int(input("Ingrese n: "))
    while not n < 200:
        n = int(input("Ingrese n: "))
    # print(fib(n-1))
    print(fibonacci(n))
main()