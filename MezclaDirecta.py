class MezclaDirecta():
    def OrdenarMezclaDirecta(self, lista):
        #print (lista)
        j = k = 0
        listaOrdenada = []
        if len(lista) > 1:
            nElementosIzq = int(len(lista) / 2)
            nElementosDer = len(lista) - nElementosIzq
            listaIzq = []
            listaDer = []
            # Copiando elementos de la lista para la listaIzquierda
            for a in range(0, nElementosIzq, 1):
                listaIzq.append(lista[a])

            # Copiando elementos de la lista para la listaDerecha
            for b in range(nElementosIzq, (nElementosIzq + nElementosDer), 1):
                listaDer.append(lista[b])

            # Recursividad
            #print("Usando la recursividad")
            #print("Lista izquierda antes de la recursividad")
            #print("-----------------------------------------")
            #print(listaIzq)
            listaIzq = self.OrdenarMezclaDirecta(listaIzq)
            #print("Usando la recursividad")
            #print("Lista derecha antes de la recursividad")
            #print("-----------------------------------------")
            #print(listaDer)
            listaDer = self.OrdenarMezclaDirecta(listaDer)
            while(len(listaIzq) != j and len(listaDer) != k):
                if (listaIzq[j] < listaDer[k]):
                    listaOrdenada.append(listaIzq[j])
                    j += 1
                else:
                    listaOrdenada.append(listaDer[k])
                    k += 1
            while(len(listaIzq) != j):
                listaOrdenada.append(listaIzq[j])
                j += 1
            while(len(listaDer) != k):
                listaOrdenada.append(listaDer[k])
                k += 1
            #print("Saliendo de la recursividad")
            #print(listaOrdenada)
            #print("-----------------------------------------")
            return listaOrdenada
        else:
            #print("Saliendo de la recursividad")
            #print(lista)
            #print("-----------------------------------------")
            return lista

def main():
    A = [9,3,1,4,5,7,2,20,55]
    b = MezclaDirecta()
    print(b.OrdenarMezclaDirecta(A))

