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


def fun1t1(anInf, anSup):
    lsArch = ["club,jugador,partidos,minutos,goles,tiros,año\n", "(JUV),Cristiano Ronaldo,29,2634,25,162,2016\n",
              "(PSG),Neymar,30,2694,13,105,2016\n", "(BAR),Lionel Messi,32,2910,37,179,2016\n",
              "(RMA),Eden Hazard,36,3101,16,77,2016\n", "(TOT),Dele Alli,35,3182,18,95,2016\n",
              "(BAR),Lionel Messi,32,3123,33,197,2017\n", "(JUV),Cristiano Ronaldo,27,2375,26,178,2017\n",
              "(BAR),Lionel Messi,29,2049,36,170,2018\n", "(JUV),Cristiano Ronaldo,30,2857,21,177,2018\n",
              "(PSG),Angel di Maria,28,2418,12,97,2018\n", "(PSG),Neymar,16,1517,15,34,2018\n",
              "(RMA),Eden Hazard,32,3115,16,93,2018\n", "(PSG),Angel di Maria,23,2106,8,74,2019\n", "(JUV),Cristiano Ronaldo,5,197,8,26,2020\n"]

    lstAux = lsArch[1:]
    lstDatos = list()
    for i in lstAux:
        i = i[:-1]
        dato = i.split(",")
        dato[5] = int(dato[5])
        dato[6] = int(dato[6])
        lstDatos.append(dato)

    for k in lsArch[:1]:
        k = k[:-1]
        titulo = k.split(",")
    lstTitulo = (titulo)

    lst1 = list()
    dic = dict()
    for j in lstDatos:
        if (j[6] >= anInf and j[6] <= anSup):
            club = j[0]
            tiros = j[5]
            anio = j[6]
            tupla = (club, tiros, anio)
            lst1.append(tupla)

    bubbleSort(lst1)

    if (len(lst1) > 0):
        lst1 = lst1[0]

    dic = dict()
    for m in lst1:
        dic[lstTitulo[6]] = lst1[2]
        dic[lstTitulo[0]] = lst1[0]
        dic[lstTitulo[5]] = lst1[1]

    return dic


def main():
    print(fun1t1(2019, 2020))
    print(fun1t1(2016, 2016))
    print(fun1t1(2020, 2020))
    print(fun1t1(2025, 2029))


main()
