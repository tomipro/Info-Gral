def buscarMin(lst):
    minimo = lst[0][1]
    id = lst[0][1]
    for i in lst:
        if i[1] < minimo:
            minimo = i[1]
            id = i[0]
    tupla = tuple([str(id), minimo])
    return tupla

def minimos(lstEnergia):
    lst = []
    for i in lstEnergia:
        linea = i.split(",")
        linea[0] = int(linea[0])
        linea[1] = int(linea[1])
        linea[2] = float(linea[2])
        lst.append(linea)
    lst_aa = []
    for j in lst:
        aa = j[0] // 10000
        energia = 0
        for k in lst:
            if k[0] // 10000 == aa:
                energia += k[2]
        if [aa, energia] not in lst_aa:
            lst_aa.append([aa, energia])
    lst_aamm = []
    for a in lst:
        aamm = a[0] // 100
        energia = 0
        for b in lst:
            if b[0] // 100 == aamm:
                energia += b[2]
        if [aamm, energia] not in lst_aamm:
            lst_aamm.append([aamm, energia])
    print([buscarMin(lst_aa),buscarMin(lst_aamm)])


def main():
    print("Prueba para el EJ01")
    lstEnergia = ['101205,1,24.2\n', '110607,8,54.4\n', '120318,3,18.1\n',
    '090501,9,88.4\n', '101209,1,26.8\n', '101217,3,22.4\n', '190101,8,44.0\n']
    (minimos(lstEnergia))
main()


# def minimos(lstEnergia):
#     dic = {}
#     for linea in lstEnergia:
#         linea = linea.split(",")
#         linea[1] = int(linea[1])
#         linea[2] = float(linea[2])
#         dic[linea[0]] = [linea[1], linea[2]]
#     print(dic)
#     # energia = float()
#     minimo = dic[0][1]
#     for key in dic:
#         if dic[key][1] < minimo:
#             minimo = dic[key][1]
#             id_minimo = key
#     energia = dic[id_minimo][1]
#     print(minimo)
#     print(energia)