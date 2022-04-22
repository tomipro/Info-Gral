from random import randint

def cargarListaAleatoria(can, a, b):
    lst = []
    for i in range(can):
        num = randint(a, b)
        lst.append(num)
    return lst

def atributoTriple(lst):
    cont = 0
    triples = 0
    aux = []
    for i in range(0, len(lst), 3):
        if lst[i] == lst[i + 1]:
            if lst[i + 1] == lst[i + 2]:
                triples += 1
    return triples
    
def main():
    # can = int(input("Ingrese cantidad: "))
    # a = int(input("Ingrese limite inferior: "))
    # b = int(input("Ingrese limite superior: "))
    # lst = cargarListaAleatoria(can, a, b)
    lst = [1, 2, 2, 2, 3, 1, 1, 3, 2]
    print(lst)
    print(atributoTriple(lst))
main()


'''
lst
index
lst 0 ? = lst 1
if true:
    lst 1 ?= lst 2
lst lst 2 ?= lst 3






'''