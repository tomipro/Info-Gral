def booleana(a,b,c):
    if a>b and b>c:
        mayor=a
        medio=b
        menor=c
    elif a>b and a>c:
        mayor=a
        medio=c
        menor=b
    elif b>c and c>a:
        mayor=b
        medio=c
        menor=a
    elif b>c and b>a:
        mayor=b
        medio=a
        menor=c
    elif c>a and a>b:
        mayor=c
        medio=a
        menor=b
    else:
        mayor=c
        medio=b
        menor=a
    if (mayor+menor)/2==medio:
        return True
    else:
        return False
         
def main():
    a=int(input("Ingrese el primer número: "))
    b=int(input("Ingrese el segundo número: "))
    c=int(input("Ingrese el tercer número: "))
    if booleana(a,b,c):
        respuesta=1
    else:
        respuesta=0
    frase=(1-respuesta)*'NO '
    print(f"{frase}Están igualmente distanciados!")
    
main()