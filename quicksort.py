class QuickSort:
    def intercambia(self, A, x, y):
        tmp = A[x]
        A[x] = A[y]
        A[y] = tmp

    def Particionar(self, A, p, r):
        x = A[r]
        i = p - 1
        for j in range(p, r):
            if (A[j] <= x):
                i = i + 1
                self.intercambia (A, i, j)
        self.intercambia(A, i+1, r)
        return i + 1

    def QuickSort(self, A, p, r):
        if (p < r):
            q = self.Particionar(A, p, r)
            #print (A[p:r])
            self.QuickSort(A, p, q-1)
            self.QuickSort(A, q+1, r)
        return A

    def ordenar(self, A):
        p = 0
        r = len(A) - 1
        q = int((p + r) / 2)
        return self.QuickSort(A, p, r)

a = [78, 67, 34, 35, 89, 56]
print (a)
b = QuickSort()
print (b.ordenar(a))