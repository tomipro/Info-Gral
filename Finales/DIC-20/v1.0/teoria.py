"""
#ej 01
#rta: E) No imprime, error. nunca se declaro variable i (contador)

def fun(lst,val):
    encontro=False
    while i<len(lst) and not encontro:
        if val<lst[i]:
            encontro=True
        else:
            i+=1
    lst.insert(i,val)

def main():
    lst = ['b', 'd', 's']
    fun(lst,'c')
    print(lst)
main()

#ej 02
#rta: F) no imprime, error. ocurre ya que no se ajusta el largo despues de sacar un indice

def fun(lst, val):
    i=0
    largo=len(lst)
    while i < largo:
        if lst[i]==val:
            lst.pop(i)
        else:
            i+=1
        
def main():
    lst = [2,4,2,6,2]
    fun(lst,2)
    print(lst)

main()

#ej 03
#rta:

import random
def main():
    num= int('123456789')
    b=10
    e=0
    e=random.randint(e,e)
    print( ((num//(b**e)) % (b**e)) % (b**e) )

main()
main()


#ej 04
#rta: B) dict vacio ya que: 1. no se modifica dict 2. no se retorna dic en fun
def fun(lst,di):
    di={}
    i=len(lst)-1
    for item in lst:
        clave = lst[i]
        di[clave]= item
        i-=1
def main():
    di={}
    lst=['a','b','c','d']
    fun(lst, di)
    print(di)

main()

def fun(a,b,c):
    p = a and(b or c)
    q = (a and b) or (a and c)
    if p == q:
        res = 10
    else:
        res = -10
    return res
def main():
    res = fun(True,True,True) + fun(True,True,False)
    print(res)
main()
"""
