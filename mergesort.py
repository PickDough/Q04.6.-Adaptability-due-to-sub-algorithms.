import random

from Insertion import Insertion
from Selection import Selection
class Merge():
    @staticmethod
    def __merge(array, aux, low, mid, high):
        for i in range(low, high+1):
            aux[i] = array[i]
        i, j = low, mid+1
        for k in range(low, high+1):
            if i > mid:
                array[k] = aux[j]
                j = j + 1
            elif j > high:
                array[k] = aux[i]
                i = i + 1
            elif aux[j] < aux[i]:
                array[k] = aux[j]
                j = j + 1
            else:
                array[k] = aux[i]
                i = i + 1
    @staticmethod
    def __adaptsort(array, aux, low, high, small, sorter):
        if high - low <= small:
            sorter.sort(array, low, high)
            return
        mid = (high+low)//2
        Merge.__adaptsort(array, aux, low, mid, small, sorter)
        Merge.__adaptsort(array, aux, mid+1, high, small, sorter)
        Merge.__merge(array, aux, low, mid, high)

    @staticmethod
    def __sort(array, aux, low, high):
        if high <= low:
            return
        mid = (high + low) // 2
        Merge.__sort (array, aux, low, mid)
        Merge.__sort (array, aux, mid + 1, high)
        Merge.__merge (array, aux, low, mid, high)

    @staticmethod
    def sort(array, adaptive=False, small=None, sorter=None):
        aux = [None]*len(array)
        if adaptive:
            Merge.__adaptsort(array, aux, 0, len(array)-1, small, sorter)
        else:
            Merge.__sort(array, aux, 0, len(array)-1)


# array = [random.randrange(1, 10000) for i in range(10000)]
# print(array)
# Merge.sort(array, True, 9, Insertion)
# print()
# print()
# print(array)