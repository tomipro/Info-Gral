# IG FINAL TEÓRICO SIN FECHA

# EJ.T.1
'''
def fun(ls, ini):
    i = ini
    while i < len(ls):
        aux = ls.pop(0)
        ls.append(aux)
        i += 1


def main():
    x = [44, 20, 14, 22, 96, 12]
    fun(x, len(x) - 1)
    print(x)


main()

¿Que imprime al ejectuar el codigo?

    a) [20, 14, 22, 96, 12, 44]
    b) [44, 20, 14, 22, 96, 12]
    c) [14, 22, 96, 12, 44, 20]
    d) [20, 14, 22, 96, 12, None]
    e) [None, None, None, None, None, None]
    f) []
    g) Ninguna de las respuestas son correctas.

RTA: a)

El ciclo while en la funcion fun solo corre una vez ya que esa condicion se cumple por unica vez.
El metodo pop() modifica la lista ls y al mismo tiempo asigna ese valor a la variable aux.
Luego el metodo append() modifica la lista ls agregandole el valor asignado a la variable aux, osea, 44.
Se le suma 1 al contador i y se imprime la lista ls que sufrio cambios despues del llamado a fun.

'''

# EJ.T.2


'''
def fun(di, nom, parcial, valor):
    if di.get(nom) != None:
        i = di.get(nom)[1]
        if di[nom][i]["a"].get(parcial) == None:
            di[nom][i]["a"][parcial] = valor


def main():
    x = {"Juan": [{"a": {"pp1": "A", "pp2": "D"}}, 0], "Lola": [{"p1": {
        "pp2": "A", "pp3": "A-"}}, 1], "Charly": [{746: {"pp1": "A", "pp3": "A-", }}, 2]}
    fun(x, "Juan", "pp3", "A")
    print(x["Juan"])


main()


¿Que imprime al ejecutar el codigo?

    a) {'a': {'pp1': 'A', 'pp2': 'D', 'pp3': 'A'}}
    b) None
    c) [{'a': {'pp1': 'A', 'pp2': 'D', 'pp3': 'A'}}, 0]
    d) [{"a": {"pp1": "A", "pp2", "D"}}, 0]
    e) {"a":{"pp1":"A","pp2":"D"}}
    f) Ninguna de las respuestas son correctas.

RTA: c)

'''

# EJ.T.3
'''
def fun(var):
    miVar = [50, 20, 10]
    aux = -10
    for i in range(0, len(var) - 1):
        for j in range(i + 1, len(var)):
            if var[i] > var[j]:
                var[i] = var[j]
                var[j] = var[i]

def main():
    miVar = [44, 22, 11]
    fun(miVar)
    print(miVar)

main()

¿Que imprime al ejecutar el codigo?

    a) [-10, -10, -10]
    b) [11, 11, 11]
    c) [10, 10, 10]
    d) [50, 20, 10]
    e) [44, 22, 11]
    f) []
    g) Ninguna de las respuestas son correctas.

RTA: b)

'''

# EJ.T.4

