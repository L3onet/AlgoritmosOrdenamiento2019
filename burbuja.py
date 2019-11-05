class Burbuja:
    def ordenamientoBurbuja(self, lista):
        for i in range(1, len(lista)):
            for j in range (len(lista)-1):
                if lista[j]>lista[j+1]:
                    temp = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = temp
        return lista