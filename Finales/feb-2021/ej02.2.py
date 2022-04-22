def bubbleSort(lista):
    n = len(lista)
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if lista[j][1] < lista[j + 1][1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp

def energiaTotal(n, lstEnergia, lstParque):
    energia = []
    for i in lstEnergia:
        dato = i.split(",")
        dato[0] = int(dato[0])
        dato[1] = int(dato[1])
        dato[2] = float(dato[2])
        energia.append(dato)
    parque = []
    for j in lstParque:
        dato = j.split(",")
        dato[0] = int(dato[0])
        dato[2] = int(dato[2])
        parque.append(dato)
    info = []
    for k in parque:
        id_parque = k[0]
        nombre = k[1]
        cantidadMolinos = k[2]
        energia_total = float()
        for e in energia:
            if id_parque == e[1]:
                energia_total += e[2]
        info.append([nombre, energia_total, energia_total / cantidadMolinos])
    bubbleSort(info)
    aux = []
    for x in range(n):
        aux.append(info[x])
    return aux

def main():
    print("Prueba para el EJ02")
    lstEnergia = ['101205,1,24.2\n', '110607,8,54.4\n', '120318,3,18.1\n',
    '090501,9,88.4\n', '101209,1,26.8\n', '101217,3,22.4\n', '190101,8,44.0\n']
    lstParque = ['1,Rosario,8\n', '6,San Martin,4\n', '8,Lavalle,10\n',
    '3,Esperanza,3\n', '7,General Pico,9\n', '9,P.Madryn,4\n']
    print(energiaTotal(3, lstEnergia, lstParque))
main()