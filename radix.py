import math

class Radix:
    def counting_sort(self, A, digit, radix):
        # "A" es una lista para ordenar, radix es la base del sistema de números, digit es el dígito
        # que queremos ordenar

        # crear una lista B que será la lista ordenada
        B = [0] * len(A)
        C = [0] * int(radix)
        # cuenta el número de ocurrencias de cada dígito en A
        for i in range(0, len(A)):
            digit_of_Ai = (A[i] / radix ** digit) % radix
            C[int(digit_of_Ai)] = C[int(digit_of_Ai)] + 1
            # ahora C[i] es el valor del número de elementos en A igual a i

        # este bucle FOR cambia C para mostrar el número acumulado de dígitos hasta ese índice de C
        for j in range(1, radix):
            C[j] = C[j] + C[j-1]
            # aquí C se modifica para tener el número de elementos <= i
        for m in range(len(A)-1, -1, -1): # para contar hacia atrás (pasar por A hacia atrás)
            digit_of_Ai = (A[m] / radix ** digit) % radix
            C[int(digit_of_Ai)] = C[int(digit_of_Ai)] -1
            B[C[int(digit_of_Ai)]] = A[m]
        return B

    def radix_sort(self, A, radix):
        # radix es la base del sistema numérico
        # k es el número más grande en la lista
        k = max(A)
        # output es la lista de resultados que construiremos
        output = A
        # calcular el número de dígitos necesarios para representar k
        digits = int(math.floor(math.log(k, radix)+1))
        for i in range(digits):
            output = self.counting_sort(output,i,radix)
        return output

a = Radix()
alist = [9,3,1,4,5,7,7,2,2]
#print (a.counting_sort(alist,0,10))

A = [9,3,1,4,5,7,7,2,20,55]
#A = [10,1,100,8]
print (a.radix_sort(A,10))