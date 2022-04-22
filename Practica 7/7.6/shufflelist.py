import random
import time

"""
def fisherYates(lst):
    for i in range(len(lst)-1, 0, -1):
        j = random.randint(0, i+1)
        lst[i], lst[j] = lst[j], lst[i]
    return lst
"""

def shuffle(lst):
    lstAux = []
    for j in range(len(lst)):
        k = random.randint(0, len(lst) - 1)
        elemento = lst.pop(k)
        lstAux.append(elemento)
    return lstAux

def main():
    i = 1
    while i <= 100:
        print(f"{i:<3}", shuffle(["a", "b", "c", "d", "e", "f", "g"]))
        # print(f"{i:<3}", fisherYates(["a", "b", "c", "d", "e", "f", "g"]))
        time.sleep(0.1)
        i += 1
main()