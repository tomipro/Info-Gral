# IG FINAL TEÓRICO 23/02/21

---

# EJ.T.1

```python
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
    a = random.randint(0,1)
    b = random.randint(0,1)
    print("{1:d} {0:d}".format(fun(a, b),fun(b, a)))

main()
```

**Indicarla respuesta correcta que resulta de ejecutar el código**

    a) Imprime SIEMPRE los valores -> 20 20
    b) Imprime SIEMPRE el valor -> 20
    c) Imprime SIEMPRE los valores -> 50 50
    d) Imprime SIEMPRE el valor -> 50
    e) Lo que imprime DEPENDE EXCLUSIVAMENTE de los valores pasados a la función 'fun'
    f) No imprime. Hay un ERROR cuando se ejecuta el código.
    g) NINGUNA de las respuestas son correctas.

**RESPUESTA CORRECTA:** *e)*

Depende de los valores de a y b que se pasan como parametro en fun. 
Si a resulta ser distinto de b, esto causa que fun retorne valores distintos comparado con si los valores de a y b
son iguales.

---

# EJ.T.2

```python
def fun(lst):
    lst += [4, 5, 6]
    lst.pop(6)
    return lst


def main():
    lst = [1, 2, 3]
    fun(lst)
    print(lst)


main()
```

**¿Qué imprime al ejecutar el código?**
    
    a) [4,5]
    b) [1,2,3,4,5,6]
    c) [1,2,3]
    d) [ ]
    e) [4,5,6]
    f) [1,2,3,4,5]
    g) No imprime. Hay un ERROR cuando se ejecuta el código.
    h) NINGUNA de las respuestas son correctas.

**RESPUESTA CORRECTA:** *g)*

La lista *lst* se modifica cuando se llama la funcion *fun*. Esta funcion le agrega 3 elementos a la lista. En la linea 3, se utiliza el metodo *pop()* para remover el elemento que se ubica en el indice 6.
Mientras si existen 6 elementos, los indices se cuentan desde 0 (0 siendo el primer indice correspondiente al primer elemento).
El indice maximo que existe en *lst* es indice 5 y se quiere usar *pop()* para el indice 6, el cual **no existe**.

*No se puede remover un elemento de una lista en un indice que no existe y por lo tanto, Python genera un error:*

![EJ.T.2](/Finales/FEB-21_B/imgs/EJ.T.2.png)

---

# EJ.T.3

```python
def fun(lst):
    lst[0][1] = '12'
    suma = 0
    for per in lst:
        suma += int(per[1])
    return suma / len(lst)

def main():
    lst = [("Paula", '10'), ("Lucas", '20'), ("Andrea", '15')]
    print("{:.2f}".format(fun(lst)))

main()
```


**¿Qué imprime al ejecutar el código?**

    a) 12.00
    b) 15
    c) 0
    d) 15.00
    e) 15.67
    f) No imprime. Hay un ERROR cuando se ejecuta el código.
    g) NINGUNA de las respuestas son correctas.

**RESPUESTA CORRECTA:** *f)*

En la linea 2 dentro de la funcion *fun*, se intenta modificar una tupla dentro de la lista *lst*. 
Esto **no** se puede hacer ya que ***las tuplas son inmutables*** (las listas si lo son).
Ya que las tuplas no se pueden modificar, Python genera un error:

![EJ.T.3](/Finales/FEB-21_B/imgs/EJ.T.3.png)

---

# EJ.T.4

**FIGURA A IMPRIMIR:**

```python
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
```

*Ejercicio resuelto:*

```python
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
```

**Indicar cual de la respuesta es la __ CONDICIÓN __ que se debe colocar en el if de la función figura() para imprimir la figura que se encuentra arriba (rombo de asteriscos).**

    a) f >= (c-(b//2)) or f <= (c+(b//2)) or f + c <= (b-1+(b//2)) or f + c >= (b-1-(b//2))
    b) f >= c or f <= c and f + c <= b or f + c >= b
    c) f >= c and f <= c and f + c <= b and f + c >= b
    d) f >= c or f <= c or f + c <= b or f + c >= b
    e) f >= (c-(b//2)) and f <= (c+(b//2)) and f + c <= (b-1+(b//2)) and f + c >= (b-1-(b//2))
    f) True
    g) Ninguna de las respuestas (CONDIONES) son correctas.

**REPUESTA CORRECTA:** *a)*

---

# EJ.T.4

```python
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
```

**¿Qué imprime al ejecutar el código?**

    a) [1,2,3,4,5]
    b) [5,4,3,2,1]
    c) []
    d) [1,1,1,1,1]
    e) [5,5,5,5,5]
    f) No imprime. Hay un ERROR cuando se ejecuta el código.
    g) NINGUNA de las respuestas son correctas

**RESPUESTA CORRECTA:** *b)*

```python
[5, 4, 3, 2, 1]
```

Los valores de la lista se intercambian entre si desde afuera hacia adentro hasta llegar al medio de la lista ('pivot').
Termina invirtiendo el sentido de la lista.