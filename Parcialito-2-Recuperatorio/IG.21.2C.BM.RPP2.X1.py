import math
def validar(num, cDig):
    largo = int(math.log10(num))
    izq = int(num // math.pow(10, largo - (cDig - 1)))
    der = int(num % (10 ** cDig))
    return (izq == reversa(der))

def reversa(num):
    numRev = 0
    while num > 0:
        resta = num % 10
        numRev = (numRev * 10) + resta
        num = num // 10
    return numRev

def main():
    num = 2589352
    cDig = 2
    print(validar(num, cDig))
main()
