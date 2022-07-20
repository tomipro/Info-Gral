# EJ.T.1

'''
import random


def fun(a, b):
    x = not (a and b)
    y = not a and not b
    if x != y:
        res = 50
    else:
        res = 20
    return res


def main():
    
    for i in range(0, 11):
        a = random.randint(0, 1)
        b = random.randint(0, 1)
        # print("{:d}: {1:d} {0:d}".format(i, fun(a, b), fun(b, a)))
        print(f"{i}: {fun(a,b)} {fun(b,a)}")


main()

Indicarla respuesta correcta que resulta de ejecutar el código
    a) Imprime SIEMPRE los valores -> 20 20
    b) Imprime SIEMPRE el valor -> 20
    c) Imprime SIEMPRE los valores -> 50 50
    d) Imprime SIEMPRE el valor -> 50
    e) Lo que imprime DEPENDE EXCLUSIVAMENTE de los valores pasados a la función 'fun'
    f) No imprime. Hay un ERROR cuando se ejecuta el código.
    g) NINGUNA de las respuestas son correctas.

RTA: e)

Depende de los valores de a y b que se pasan como parametro en fun. 
Si a resulta ser distinto de b, esto causa que fun retorne valores distintos comparado con si los valores de a y b
son iguales.

'''

# EJ.T.2

'''
def fun(lst):
    lst += [4, 5, 6]
    lst.pop(6)
    return lst


def main():
    lst = [1, 2, 3]
    fun(lst)
    print(lst)


main()


¿Qué imprime al ejecutar el código?
    
    a) [4,5]
    b) [1,2,3,4,5,6]
    c) [1,2,3]
    d) [ ]
    e) [4,5,6]
    f) [1,2,3,4,5]
    g) No imprime. Hay un ERROR cuando se ejecuta el código.
    h) NINGUNA de las respuestas son correctas.

RTA: g)

La lista lst se modifica cuando se llama la funcion fun. Esta funcion le agrega 3 elementos a la lista.
En la linea 3, se utiliza el metodo pop() para remover el elemento que se ubica en el indice 6.
Mientras si hay 6 elementos, los indices se cuenta desde 0 (0 siendo el primer indice correspondiente al primer elemento).
El indice maximo que existe en lst es indice 5 y se quiere usar pop() para el indice 6, el cual no existe.
No se puede remover un elemento de un indice que no existe y por lo tanto, Python genera un error.
'''

# EJ.T.3

'''
def fun(lst):
    lst[0][1] = '12'
    suma = 0
    for per in lst:
        suma += int(per[1])
    return suma / len(lst)

def main():
    lst = [("Paula",'10'),("Lucas",'20'),("Andrea",'15')]
    print("{:.2f}".format(fun(lst)))

main()


¿Qué imprime al ejecutar el código?

    a) 12.00
    b) 15
    c) 0
    d) 15.00
    e) 15.67
    f) No imprime. Hay un ERROR cuando se ejecuta el código.
    g) NINGUNA de las respuestas son correctas.

RTA: f)

En la linea 2 dentro de la funcion fun, se intenta modificar una tupla dentro de la lista lst. 
Esto no se puede hacer ya que las tuplas son inmutables (las listas si lo son).
Ya que las tuplas no se pueden modificar, Python genera un error:

'''


# EJ.T.4

# # # # # # # # # # # # # # # # # # # # # # #
# # F I G U R A A I M P R I M I R # #
'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
# # # # # # # # # # # # # # # # # # # # # # #

#ejercicio resuelto

def figura(b):
    for f in range(0, b):
        for c in range(0, b):
            if (f >= (c - (b//2)) and f <= (c + (b//2)) and f + c <= (b - 1 + (b // 2)) and f + c >= (b - 1 - (b // 2))):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    

def main():
    figura(9)
main()

'''

# EJ.T.5

'''
def fun(x):
    i = 0
    tam = len(x)
    while i < (tam/2):
        a = x[i]
        x[i] = x[tam - 1 - i]
        x[tam - 1 - i] = a
        i += 1

def main():
    x = [1, 2, 3, 4, 5]
    fun(x)
    print(x)

main()


¿Qué imprime al ejecutar el código?

    a) [1,2,3,4,5]
    b) [5,4,3,2,1]
    c) []
    d) [1,1,1,1,1]
    e) [5,5,5,5,5]
    f) No imprime. Hay un ERROR cuando se ejecuta el código.
    g) NINGUNA de las respuestas son correctas

RTA: b)

[5, 4, 3, 2, 1]

Los valores de la lista se intercambian entre si desde afuera hacia adentro hasta llegar al medio de la lista ('pivot').
Termina invirtiendo el sentido de la lista.

'''



'''
i = 0 
tam = 5

a = x[0] # a = 1
x[0] = x[5 - 1 - 0]      #x[0] = x[4]
x[5 - 1 - 0] ] = a     #x[4] = x[0]
i +=1 

i = 1

a = x[1] # a = 2
x[1] = x[5-1-1] -> x[1] = x[3]
x[4] = 2
i += 1

i = 2
a = x[2] -> a = 3
x[2] = x[2]
x[2] = 3

i+= 1

end while


x = [5, 4, 3, 2, 1]
'''

