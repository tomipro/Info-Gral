from collections import Counter
import json

def fun():
    archivo = open("/Users/tomasprodan/Documents/Info GRAL/Practica 7/7.3/pinocho.txt", "r")
    lst = [linea.split() for linea in archivo]
    archivo.close()
    palabras = []
    for pal in lst:
        palabras += pal
    contador = dict(Counter(palabra for frase in palabras for palabra in frase.split()))
    return contador

def genArchivo():
    target = open("/Users/tomasprodan/Documents/Info GRAL/Practica 7/7.3/frecuencias.csv", "w")
    target.write(str(fun()))
    target.close()
genArchivo()

def txt_a_json():
    with open("/Users/tomasprodan/Documents/Info GRAL/Practica 7/7.3/7.3.json", "w") as saliente:
        json.dump(fun(), saliente, indent = 4)
txt_a_json()

# print(fun("/Users/tomasprodan/Documents/Info GRAL/Practica 7/7.3/pinocho.txt"))
