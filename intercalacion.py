class OrdenamientoIntercalacion:
    def Intercalar(self, lista1, lista2):
        lista3 = []
        i = j = 0
        tamLista3 = len(lista1) + len(lista2)
        for k in range(0, tamLista3, 1):
            if (j == len(lista2) and k < tamLista3):
                lista3.append(lista1[i])
                i += 1
            if (i == len(lista1) and k < tamLista3):
                lista3.append(lista2[j])
                j += 1
            if (i < len(lista1) and j < len(lista2)):
                if (lista1[i] < lista2[j]):
                    lista3.append(lista1[i])
                    i += 1
                else:
                    lista3.append(lista2[j])
                    j += 1
        return lista3

    def Merge(self, listaIzq, listaDer):
        j = k = 0
        listaOrdenada = []
        while (len(listaIzq) != j and len(listaDer) != k):
            if (listaIzq[j] < listaDer[k]):
                listaOrdenada.append(listaIzq[j])
                j += 1
            else:
                listaOrdenada.append(listaDer[k])
                k += 1
        listaOrdenada.extend(listaIzq[j:])
        listaOrdenada.extend(listaDer[k:])
        return listaOrdenada


def main():
    a = OrdenamientoIntercalacion()
    lista2 = [2,4,6,8,10,11,12,13]
    lista1 = [1,3,5,7,9]
    print(a.Merge(lista1, lista2))

if __name__ == "__main__":
    main()