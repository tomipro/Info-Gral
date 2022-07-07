# EXÁMEN TEÓRICO -  09/02/2021 

---

# EJ.T.1

```python
def fun(lst, val):
    encontro = False
    while i < len(lst) and not encontro:
        if val<lst[i]:
            encontro=True
        else:
            i += 1
    lst.insert(i, val)

def main():
    lst = ['b', 'd', 's']
    fun(lst, 'c')
    print(lst)
main()
```

**¿Qué imprime al ejecutar el código?**

    a) ['c', 'b', 'd', 's']
    b) ['b', 'd', 's', 'c']
    c) ['b', 'd', 'c', 's']
    d) ['b', 'c', 'd', 's']
    e) No imprime. Hay un error cuando se ejecuta el código.
    f) Ninguna de las respuestas son correctas.

**RESPUESTA CORRECTA:** *e)*

En la funcion *fun* se pone una condicion que depende del valor **'i'**, sin embargo, en ningun momento
se declaro el valor de **'i'**. No se puede hacer logica con un valor que no se sabe cuanto es, y por lo tanto
Python tira un error:


![ejercicio1teoria](/Finales/feb-2021/v2.0/imgs/ej1teoria.png)

---

# EJ.T.2

```python
def fun(lst, val):
    i = 0
    largo = len(lst)
    while i < largo:
        if lst[i] == val:
            lst.pop(i)
        else:
            i += 1

def main():
    lst = [2, 4, 2, 6, 2]
    fun(lst, 2)
    print(lst)

main()
```

**¿Qué imprime al ejecutar el código?**

    a) [2,4,2,6,2]
    b) [4,6,2]
    c) [ ]
    d) [4,2,6,2]
    e) [4,6]
    f) No imprime. Hay un error cuando se ejecuta el código.
    g) Ninguna de las respuestas son correctas.

**RESPUESTA CORRECTA:** *f)*
```
Da error al ejecutar el código
```
Ocurre porque se elimina un valor pero el len sigue siendo el mismo. Cuando se recorre una lista mas veces que la cantidad de elementos que existen, Python tira un error: 

![ejercicio3toeria](/Finales/feb-2021/v2.0/imgs/ej2teoria.png)

---

# EJ.T.3

```python
import random
def main():
    num = int('123456789')
    b = 10
    e = 0
    e = random.randint(e, e)
    print( ((num//(b**e)) % (b**e)) % (b**e) )

main()
main()
```

**¿Qué imprime al ejecutar el código?**

    a) 456456
    b) 3456
    c) 11
    d) 88
    e) 00
    f) No imprime. Hay un error cuando se ejecuta el código.
    g) Ninguna de las respuestas son correctas.

**RESPUESTA CORRECTA**: *e)*

```python
0
0
```

El operador de modulo *"%"* se utiliza para obtener el remanente de la division del numero a la izquierda por el de la derecha. La division entre un entero y 1 retorna un remanente de 0. 

---

# EJ.T.4

```python
def fun(lst, di):
    di = {}
    i = len(lst) - 1
    for item in lst:
        clave = lst[i]
        di[clave] = item
        i -= 1

def main():
    di = {}
    lst = ['a','b','c','d']
    fun(lst, di)
    print(di)

main()
```

**¿Qué imprime al ejecutar el código?**

    a) {'a': None, 'b': None, 'c': None, 'd': None}
    b) { }
    c) { [ ] : [ ] }
    d) {'d': 'a', 'c': 'b', 'b': 'c', 'a': 'd'}
    e) {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd'}
    f) No imprime. Hay un error cuando se ejecuta el código.
    g) Ninguna de las respuestas son correctas.

**RESPUESTA CORRECTA:** *b)*
```python
{}
```
El diccionario declarado en la funcion *fun* es el unico diccionario que sufre modificaciones.
El diccionario *di* en el main no es alterado. 
Esto ocurre porque en *fun* el diccionario que se pasa por parametro se llama igual que el diccionario de
alcance (scope) local y dentro de esa funcion, siempre se prioritiza.

***El scope es limitado y se mantiene dentro de la función únicamente en la que se declaran.***

---

# EJ.T.5

```python
def fun(a, b, c):
    p = a and (b or c)
    q = (a and b) or (a and c)
    if p == q:
        res = 10
    else:
        res = -10
    return res

def main():
    res = fun(True, True, True) + fun(True, True, False)
    print(res)

main()
```

**¿Qué imprime al ejecutar el código?**

    a) -20
    b) 10
    c) 0
    d) 20
    e) -10
    f) No imprime. Hay un error cuando se ejecuta el código.
    g) Ninguna de las respuestas son correctas.

**RESPUESTA CORRECTA:** *d)*

```python
20
```
La funcion *fun* retorna 10 en ambos llamados resultando en un resultado final de 20. Esto es consecuencia del *or* en la linea 3 (en el caso del segundo llamado).

---