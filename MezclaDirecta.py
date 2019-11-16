from intercalacion import *

class MezclaDirecta():
    def OrdenarMezclaDirecta(self, lista):
        if len(lista) > 1:
            mitad = len(lista) // 2
            listaIzq = lista[0:mitad]
            listaDer = lista[mitad:len(lista)]

            # Recursividad
            listaIzq = self.OrdenarMezclaDirecta(listaIzq)
            listaDer = self.OrdenarMezclaDirecta(listaDer)
            comb = OrdenamientoIntercalacion()
            listaOrdenada = comb.Merge(listaIzq, listaDer)
            return listaOrdenada
        else:
            return lista

def main():
    A = [9,3,1,4,5,7,2,20,55]
    b = MezclaDirecta()
    print(b.OrdenarMezclaDirecta(A))

if __name__ == "__main__":
    main()