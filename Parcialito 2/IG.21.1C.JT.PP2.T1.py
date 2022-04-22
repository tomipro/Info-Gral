def simplificar(num):
    carac=",()\""
    simple=""
    for i in num:
        if i not in carac:
            simple+=i
    return int(simple)

def largoNum(num):
    simple=simplificar(num)
    lar=0
    while simple>0:
        lar+=1
        simple=simple//10
    return lar

def sumatoria(num):
    simple=simplificar(num)
    largo=largoNum(num)
    suma=0
    while simple!=0:
        suma+=largo
        simple=simple//10
        largo=simple%10
    return suma

def main():
    num=(input(""))
    print(sumatoria(num))
main()