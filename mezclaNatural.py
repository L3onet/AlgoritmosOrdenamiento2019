from MezclaDirecta import *
class MezclaNatural:

    def OrdenamientoMezclaNatural(self, lista):
        aux1 = []
        aux2 = []
        aux3 = []
        mezcla = MezclaDirecta()
        izquierda = izq = 0
        derecha = len(lista) - 1
        der = derecha
        ordenado = False
        while True:
            ordenado = True
            izquierda = 0
            while izquierda < derecha:
                izq = izquierda
                while izq < derecha and lista[izq] <= lista[izq + 1]:
                    izq += 1
                aux1 = lista[izquierda:izq+1]
                der = izq + 1
                while der == derecha or der < derecha and lista[der] <= lista[der + 1]:
                    der += 1
                aux2 = lista[izq+1:der+1]
                aux3 = lista[der+1:len(lista)]
                if len(aux3) > 0:
                    if aux2[len(aux2) - 1] < aux3[0]:
                        aux2.extend(aux3)
                        aux3.clear()
                    else:
                        aux1.extend(aux3)
                        aux3.clear()
                lista = mezcla.combinar(aux1, aux2)
                if len(aux2) == 0 and len(aux3) == 0:
                    ordenado = True
                    break
            if ordenado != False:
                break
        return lista

def main():
    A = [9,3,1,4,5,7,7,2,2]
    b = MezclaNatural()
    print(b.OrdenamientoMezclaNatural(A))

if __name__ == "__main__":
    main()