"""

def fun(t,a):
    i = len(t)
    while i < len(t) and t[i] < a:
        i += 1
    return t[:i] + [a] + t[i:]    
"""
"""

def main():
    x = [10, 20, 30, 40, 50]
    x = fun(x, 6)
    print(x)
main()
def fun(data,k,v):
    if data.get(k) == None:
        data[k] = v


def main():
    x = {"Buenos Aires":{"Tandil":{"sup":447,"pob":1190}}, "San Luis":{"Merlo":{"sup":321,"pob":999}},"Corrientes":{"Goya":{"sup":1234,"pob":999}}}
    fun(x, "Corrientes",{"Esquina":{"sup":666,"pob":333}})
    print(x["Corrientes"])
main()

"""
'''
def figura(b):
    for  f in range(0,b):
        for c in range(0, b):
            if 
def fun(var):
    aux = -10
    for a in range(len(var)-1):
        for b in range(a+1, len(var)):
            if var[a] < var[b]:
                var[b] = aux
                aux = var[b]

def main():
    miVar = [23,45,10]
    fun(miVar)
    print(miVar)
main()

'''