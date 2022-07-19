# EJ.T2 TEMA-1

'''
def fun(data, k):
    for key in data.keys():
        if data[key] == data.get(k):
            data[key] = "***"
        elif data.get(k) != None:
            data[key] = "###"


def main():
    d = {(22, "go"): "Google",
         (7, "aa"): "Apple",
         (18, "mi"): "microsoft"}
    fun(d, (7, "aa"))
    print(d)


main()
'''

# EjT3.T1


'''
def aMay(x):
    if x[0] in "abcdefghaijklmnñopqrstuvwxyz":
        x = chr(ord(x[0])-32) + x[1:]
    return x


def fun(var):
    i = 0
    while i < len(var):
        var[i] = aMay(var[i])
        i += 1


def main():
    miVar = ["belen", "andres", "diego"]
    fun(miVar)
    print(miVar)


main()

'''

# EjT5.T2


'''
def fun(ls, va):
    i = 0
    while i < len(ls):
        if va == ls[i]:
            ls.pop(i)
        else:
            i += 1


def main():
    lst = ["a", "b", "x", "x", "c"]
    fun(lst, "x")
    print(lst)


main()
'''


'''
def fun(t, a):
    i = 0
    while i < len(t) and t[i] > a:
        t[i] = a
        i += 1
    return t[:i]


def main():
    x = [10, 20, 30, 40, 50]
    x = fun(x, 1)
    print(x)


main()

'''

# EJ.T4 TEMA-1
'''
def figura(b):
    for f in range(0, b):
        for c in range(0, b):
            if (((f + c <= b - 1) and f >= c) or (f == b//2)):
                print(" *", end="")
            else:
                print("  ", end="")
        print()


def main():
    figura(7)


main()
'''