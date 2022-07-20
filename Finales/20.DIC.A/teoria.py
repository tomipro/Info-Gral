# EJ.T.1

'''
def fun(nombres):
    nombres.insert(1, 'Charly')
    nombres = nombres[:-1]


def main():
    names = ['Tom', 'Tommy', 'Tomas']
    fun(names)
    print(names)

main()

¿Qué imprime al ejecutar el código?
    a) ['Tom', 'Tommy', 'Tomas']
    b) ['Tom', 'Charly', 'Tommy']
    c) ['Tom', 'Charly', 'Tommy', 'Tomas']
    d) Da error al ejecutar el código
    e) Ninguna de las anteriores

RTA: c) ['Tom', 'Charly', 'Tommy', 'Tomas']
insert es un metodo que modifica el parametro que se le pasa
como no se retorna nada, lo unico que modifica mi lista original es el insert

'''

# EJ.T.2

'''
def main():
    num= int('123456789')
    b=10
    e=3
    print( ((num//(b**e)) % (b**e)) % (b**e) )
main()

¿Qué imprime al ejecutar el código?
    a) 456
    b) 3456
    c) 0
    d) 1
    e) Da error al ejecutar el código
    f) Ninguna de las anteriores

RTA: a) 456
ocurre porque division entera me saca los digitos de la derecha
modulo me saca de la izquierda

'''

# EJ.T.3

'''
def fun(lst, val):
    largo=len(lst)
    for i in range(0,largo):
        if lst[i]==val:
            lst.pop(i)

def main():
    lst = [1,2,3,4,4,3,2,1]
    fun(lst,2)
    print(lst)
main()

¿Qué imprime al ejecutar el código?
    a) [1,2,3,4,4,3,2,1]
    b) [1,3,4,4,3,1]
    c) [2,2]
    d) [ ]
    e) Da error al ejecutar el código
    f) Ninguna de las anteriores

RTA: e) Da error al ejecutar el código
ocurre porque se elimina un valor pero el len sigue siendo el mismo

'''

# EJ.T.4

'''
import random

def cargarDi (lst):
    di = {}
    for item in lst:
        clave = random.randint(1, 100)
        while clave in lst:
            clave = random.randint(1, 100)
        di[clave]= item
    
    return di

def main():
    lst=['Tom', 'Charly', 'Tommy', 'Tomas']
    di = cargarDi(lst)
    print(di)
main()

Algunas posible salida esperadas para el código completo podrían ser:
    {45: 'Tom', 30: 'Charly', 59: 'Tommy', 56: 'Tomas'}
    {83: 'Tom', 92: 'Charly', 33: 'Tommy', 59: 'Tomas'}
    {4: 'Tom', 11: 'Charly', 54: 'Tommy', 10: 'Tomas'}

'''


