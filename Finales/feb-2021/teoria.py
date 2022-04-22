"""
#ej 01
#rta: E) depende del valor que se le pasa a fun
import random
def fun(a,b):
    x = not(a and b)
    y = not a and not b
    if x != y:
        res = 50
    else:
        res = 20
    return res
def main():
    a = random.randint(0,1)
    b = random.randint(0,1)
    print("{1:d} {0:d}".format(fun(a,b),fun(b,a)))
main()

#ej 02
#rta: G) No imprime. Error (pasa porque no existe el indice 6)

def fun(lst):
    lst+=[4,5,6]
    lst.pop(6)
    return lst

def main():
    lst=[1,2,3]
    fun(lst)
    print(lst)

main()


#ej 03
#rta F) error. lst es una lista de tuplas, tuplas no son reasignables/transmutables

def fun(lst):
    lst[0][1]='12'
    suma=0
    for per in lst:
        suma+=int(per[1])
    return suma/len(lst)

def main():
    lst=[("Paula",'10'),("Lucas",'20'),("Andrea",'15')]
    print("{:.2f}".format(fun(lst)))
main()


#ej 05:
#rta: B) es un bubble sort

def fun(x):
    i=0
    tam=len(x)
    while i< (tam/2):
        a = x[i]
        x[i] = x[tam-1-i]
        x[tam-1-i] = a
        i+=1
def main():
    x=[1,2,3,4,5]
    fun(x)
    print(x)
main()
#ej04
#rta: 

def figura(b):
    for f in range(0,b):
        for c in range(0,b):
            if True: # <<<<< ¿Cuál es la condición?
                print(" *", end="")
            else:
                print(" ", end="")
        print()

def main():
    figura(9)
main()

"""