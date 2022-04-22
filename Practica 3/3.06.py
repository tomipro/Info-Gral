def booleana(x):
    if x%2==0:
        y=int(input(f"Ingrese un número menor que {x}: "))
    else:
        y=int(input(f"Ingrese un número mayor que {x}: "))
    if x%2==0 and y<x:
        return 1
    elif x%2==1 and y>x:
        return 1
    else:
        return 0
    
def main():
    x=int(input('Ingrese un número entero positivo: '))
    resultado=booleana(x)
    frase="Correcto!"*resultado+"Incorrecto!"*(1-resultado)
    print(frase)
main()