# EXÁMEN TEÓRICO - 01/12/2020 - Tema 1

---

# EJ.T.1

```python
def fun(nombres):
    nombres.insert(1, 'Charly')
    nombres = nombres[:-1]


def main():
    names = ['Tom', 'Tommy', 'Tomas']
    fun(names)
    print(names)

main()
```

**¿Qué imprime al ejecutar el código?**

    a) ['Tom', 'Tommy', 'Tomas']
    b) ['Tom', 'Charly', 'Tommy']
    c) ['Tom', 'Charly', 'Tommy', 'Tomas']
    d) Da error al ejecutar el código
    e) Ninguna de las anteriores

**RESPUESTA CORRECTA:** *c)*
```python
['Tom', 'Charly', 'Tommy', 'Tomas']
```

*insert()* es un metodo que modifica el parametro que se le pasa y como no se retorna nada, lo unico que modifica mi lista original es el insert.

---

# EJ.T.2

```python
def main():
    num = int('123456789')
    b = 10
    e = 3
    print( ((num//(b**e)) % (b**e)) % (b**e) )

main()
```

**¿Qué imprime al ejecutar el código?**
    
    a) 456
    b) 3456
    c) 0
    d) 1
    e) Da error al ejecutar el código
    f) Ninguna de las anteriores

**RESPUESTA CORRECTA:** *a)* 
```python
456
```
Ocurre porque la division entera me saca los digitos de la derecha y modulo me saca de la izquierda segun la cantidad de digitos que tengo.

---

# EJ.T.3

```python
def fun(lst, val):
    largo = len(lst)
    for i in range(0,largo):
        if lst[i] == val:
            lst.pop(i)

def main():
    lst = [1,2,3,4,4,3,2,1]
    fun(lst, 2)
    print(lst)

main()
```
**¿Qué imprime al ejecutar el código?**

    a) [1,2,3,4,4,3,2,1]
    b) [1,3,4,4,3,1]
    c) [2,2]
    d) [ ]
    e) Da error al ejecutar el código
    f) Ninguna de las anteriores

**RESPUESTA CORRECTA:** *e)*
```
Da error al ejecutar el código
```
Ocurre porque se elimina un valor pero el len sigue siendo el mismo. Cuando se recorre una lista mas veces que la cantidad de elementos que existen, Python tira un error: 

![ejercicio3](/Finales/DIC-20/v2.0/imgs/ej3teoria.png)

---

# EJ.T.4

*Ejercicio resuelto*

```python
import random

def cargarDi (lst):
    di = {}
    for item in lst:
        clave = random.randint(1, 100)
        while clave in lst:
            clave = random.randint(1, 100)
        di[clave] = item
    
    return di

def main():
    lst = ['Tom', 'Charly', 'Tommy', 'Tomas']
    di = cargarDi(lst)
    print(di)
main()
```

**Algunas posible salida esperadas para el código completo podrían ser:**
```python
{45: 'Tom', 30: 'Charly', 59: 'Tommy', 56: 'Tomas'}
{83: 'Tom', 92: 'Charly', 33: 'Tommy', 59: 'Tomas'}
{4: 'Tom', 11: 'Charly', 54: 'Tommy', 10: 'Tomas'}
```


---