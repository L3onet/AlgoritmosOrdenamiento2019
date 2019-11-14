class ShellSort:
    def shellSort(self, alist):
        sublistcount = len(alist) // 2
        while sublistcount > 0:
            for start_position in range(sublistcount):
                self.gap_InsertionSort(alist, start_position, sublistcount)
            #print("Después de incrementos de tamaño ", sublistcount, "la lista es", nlist)
            sublistcount = sublistcount // 2
        return alist

    def gap_InsertionSort(self, nlist, start, gap):
        for i in range(start + gap, len(nlist), gap):
            current_value = nlist[i]
            position = i
            while position >= gap and nlist[position - gap] > current_value:
                nlist[position] = nlist[position - gap]
                position = position - gap
            nlist[position] = current_value

def main():
    nlist = [14,46,43,27,57,41,45,21,70]
    b = ShellSort()
    a = b.shellSort(nlist)
    print(a)