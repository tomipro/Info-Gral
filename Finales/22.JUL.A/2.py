def bubbleSort(arr):
    n = len(arr)
    for i in range(0, n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j][1] < arr[j + 1][1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swapped = True

        if not swapped:
            return


def fun2t1(n):
    lsArch = ["club,jugador,partidos,minutos,goles,tiros,año\n", "(JUV),Cristiano Ronaldo,29,2634,25,162,2016\n",
              "(PSG),Neymar,30,2694,13,105,2016\n", "(BAR),Lionel Messi,32,2910,37,179,2016\n",
              "(RMA),Eden Hazard,36,3101,16,77,2016\n", "(TOT),Dele Alli,35,3182,18,95,2016\n",
              "(BAR),Lionel Messi,32,3123,33,197,2017\n", "(JUV),Cristiano Ronaldo,27,2375,26,178,2017\n",
              "(BAR),Lionel Messi,29,2049,36,170,2018\n", "(JUV),Cristiano Ronaldo,30,2857,21,177,2018\n",
              "(PSG),Angel di Maria,28,2418,12,97,2018\n", "(PSG),Neymar,16,1517,15,34,2018\n",
              "(RMA),Eden Hazard,32,3115,16,93,2018\n", "(PSG),Angel di Maria,23,2106,8,74,2019\n", "(JUV),Cristiano Ronaldo,5,197,8,26,2020\n"]

    lstDatos = list()
    for i in lsArch[1:]:
        i = i[:-1]
        dato = i.split(",")
        dato[2] = int(dato[2])
        dato[3] = int(dato[3])
        dato[4] = int(dato[4])
        dato[5] = int(dato[5])
        dato[6] = int(dato[6])
        lstDatos.append(dato)

    lst = list()
    for j in lstDatos:
        jugador = j[1]
        minutos = j[3]
        lst.append((jugador, minutos))

    lst2 = list()
    for k in lstDatos:
        jug = k[1]
        minJugados = 0
        for l in lst:
            if k[1] == l[0]:
                minJugados += l[1]
        if [jug, minJugados] not in lst2:
            lst2.append([jug, minJugados])

    bubbleSort(lst2)

    return lst2[:n]


def main():
    print(fun2t1(0))

    print(fun2t1(1))

    print(fun2t1(2))

    print(fun2t1(3))

    print(fun2t1(4))


main()
