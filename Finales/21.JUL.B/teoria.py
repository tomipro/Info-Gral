# EJ.T.1

'''
def comparar(a, b, c):
    if ((a and (b or c)) != ((a and b) or (a and c))):
        return True
    
    else:
        return False

# print(comparar(0, 0, 1))
¿Que retorna la función?

    a) Siempre retorna False
    b) Siempre retorna True
    c) El valor del retorno depende de los valores de las variables que se pasan por parametro
    d) No retorna nada, pues hay error de sintaxis
    e) Ninguna de las anteriores

RTA: a)

Siempre retorna False ya que la condicion en la linea 2 siempre va a ser False.
Esto ocurre porque la comparacion que se realiza es entre dos condiciones que son identicas pero escritas de otra manera.
Si se "distribuye", se ve mejor: 

(a and (b or c)) = (a and b) or (a and c)


'''

# EJ.T.2

'''
def f2(x):
    x = x + 10
    return x

def f1():
    x = 10
    print(str(f2(x)) + "-", end="")

x = 5
f1()
print("{0:d}".format(f2(x)))

¿Que imprime al ejecutar el código anterior?

    a) 20-15-20
    b) 15-20-15
    c) 15-20
    d) 20-15
    e) Ninguna de las anteriores

RTA: d)

20-15

El 20- viene del llamado a la funcion f1 en el que se llama a la funcion f1 y modifica el valor de x de 10 a 20. 
Luego se llama a la funcion f2 pasando a x = 5 como parametro, f2 modifica el valor de x de 5 a 15.

'''

# EJ.T.3

# Ejercicio resuelto

'''
def esPalindromo(palabra):
    palindromo = True
    for i in range(0, len(palabra)):
        if (palabra[len(palabra) - i - 1] != palabra[i]):
            palindromo = False
    
    return palindromo

Completar las lineas en blanco (_____), sin agregar ni cambiar renglones al código mostrado, de la 
funcion esPalindromo para que retorne True si la palabra pasado por parámetro es un palindromo
o retorne False en caso contrario. Asuma que siempre se recibe una sola palabra y esta en minusculas.
Palindromo es una palabra o expresion que es igual si se lee de izquierda a derecha que de derecha a izquierda.
Ej's: Anana, ana, rayar, ...etc.

'''

# EJ.T.4

# Ejercicio resuelto

'''
def archivoAListaDeRenglones(nombreArchivo):
    arch = open(nombreArchivo, 'r')
    lista = arch.readlines()
    arch.close()
    return lista

Completar las lineas en blanco (_____), sin agregar ni cambiar renglones al código mostrado, de la 
funcion archivoAListaDeRenglones para que la función abra y lea el archivo cuyo nombre se recibe
por parametro, para crear y retornar una lista de strings donde cada string se corresponde
con un renglón del archivo leído. 


'''