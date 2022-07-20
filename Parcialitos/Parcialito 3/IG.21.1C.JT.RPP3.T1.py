def fusion(lst1, lst2):
    lst1, lst2 = set(lst1), set(lst2)
    union_ = lst1 | lst2
    interseccion_ = lst1 & lst2
    return list(union_ - interseccion_)

def ordIns(res):
    for i in range(1, len(res)):
        a = res[i]
        j = i - 1
        while j >= 0 and res[j] > a:
            res[j + 1] = res[j]
            j -= 1
        res[j + 1] = a


def fusion2(lst1, lst2, res):
    for i in lst1:
        if i not in lst2 and i not in res:
            res.append(i)
    for i in lst2:
        if i not in lst1 and i not in res:
            res.append(i)

def main():
    lst1 = [15, 2, 6, 2, 6, 4, 10, 9, 5]
    lst2 = [7, 3, 4, 8, 3, 12, 5, 20, 3, 4]
    res = []
    fusion2(lst1, lst2, res)
    print("Fusion:", res)
    ordIns(res)
    print("Fusion Ordenada:", res)
    x = fusion(lst1, lst2)
    print("Fusion metodo 2:", x)
main()