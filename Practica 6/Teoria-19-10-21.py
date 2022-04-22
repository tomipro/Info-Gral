#CLASE 19/10/2021: INTRODUCCION A LISTAS
# lst3 = [23,3.14,22,"hola",99]

# def recorrerWhile(lst3):
#     print("WHILE:")
#     i=0
#     while (i<len(lst3)):
#         print(lst3[i], end=" ")
#         i+=1
# recorrerWhile(lst3)

# def recorrerFor(lst3):
#     print("\nFOR:")
#     for i in range(0,len(lst3)):
#         print(lst3[i], end = " ")

# recorrerFor(lst3)

# def recorrerFor2(lst3):
#     print("\nFOR:")
#     for x in lst3:
#         print(x, end = " ")
# recorrerFor2(lst3)

# lst1 = ["ES", "MU", "TA", "BLE"]
# print(" - "*6, "MUTABLE", " - "*6)
# print("Antes: -> ", lst1)
# lst1[0] = "es"
# print("Despues: - >", lst1)
# print(" - "*15)
# lst1.remove("MU")
# print("Final: - >", lst1)
# print(" - "*15)
# lst2 = lst1[:]
# print(lst2)

# lst = [10,2,9,40,25,6]
# #lst.pop() elimina ultima posicion
# #lst.pop(0) elimina primera posicion
# def eliminarEnListaPorPosicion(lst,pos):
#     res = None
#     if pos>=0 and pos<len(lst):
#         res = lst.pop(pos)
#     return res
# print(eliminarEnListaPorPosicion(lst,3))

# lst = [10,2,9,40,25,6]
# def eliminarEnListaPorValor(lst,x):
#     if x in lst:
#         lst.remove(x)
# eliminarEnListaPorValor(lst,10)
# print(lst)

# from random import randint as r
# def cargarListaAle(lst,cant,ini,fin):
#     for _ in range(0,cant):
#         valAle = r(ini,fin)
#         lst.append(valAle)

# def main():
#     lst = []
#     print("Antes->:", lst)
#     cargarListaAle(lst, 5, 10, 100)
#     print("Despues->:", lst)
# main()

#otra forma:
# from random import randint as r
# def cargarListaAle2(cant,ini,fin):
#     ls = []
#     for _ in range(0,cant):
#         valAle = r(ini,fin)
#         ls.append(valAle)
#     return ls
# def main():
#     lst = cargarListaAle2(5, 10, 100)
#     print("Despues->:", lst)
# main()

# from random import randint as r
# def procesarLista(lstEnt,cant,ini,fin):
#     lst = lstEnt[:]
#     for _ in range(0,cant):
#         valAle = r(ini,fin)
#         lst.append(valAle)
#     suma = 0
#     for x in lst:
#         suma = suma+x
#     print("La sumatoria es:",suma)

# def main():
#     ls = []
#     print("Antes->:", ls)
#     procesarLista(ls, 5, 10, 100)
#     print("Despues->:", ls)
# main()

# import random
# def ordenar(lst):
#     for i in range(0,len(lst)-1):
#         for j in range(i+1,len(lst)):
#             if lst[i]>lst[j]:      #intercambio de elementos
#                 aux = lst[i]
#                 lst[i] = lst[j]
#                 lst[j] = aux
#                 #lst[i], lst[j] = lst[j], lst[i]
                
# def cargarListaAle(ls,cant,ini,fin):    
#     for _ in range(cant):
#         valAle = random.randint(ini,fin)
#         ls.append(valAle)   
# def main():
#     lst=[]
#     cargarListaAle(lst,5,10,100)
#     print("Lista Original lst->:",lst)
#     ordenar(lst)
#     print("Lista lst Ordenada->:",lst)
# main()

