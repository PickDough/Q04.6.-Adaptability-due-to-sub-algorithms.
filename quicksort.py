import random

class QuickSort():
    @staticmethod
    def __partition(array, low, high):
        pivot_index = random.randint (low, high)
        pivot = array[pivot_index]
        i, j = low - 1, high + 1

        while True:
            while True:
                i += 1
                if array[i] >= pivot:
                    break

            while True:
                j -= 1
                if array[j] <= pivot:
                    break

            if i >= j:
                return j

            temp = array[i]
            array[i] = array[j]
            array[j] = temp

    @staticmethod
    def __adaptsort(array, low, high, small, sorter):
        if high - low <= small:
            sorter.sort(array, low, high)
            return
        j = QuickSort.__partition (array, low, high)
        QuickSort.__adaptsort(array, low, j - 1, small, sorter)
        QuickSort.__adaptsort (array, j + 1, high, small, sorter)

    @staticmethod
    def __sort(array, low, high):
        if high <= low:
            return
        j = QuickSort.__partition (array, low, high)
        QuickSort.__sort (array, low, j - 1)
        QuickSort.__sort (array, j + 1, high)

    @staticmethod
    def sort(array, adaptive=False, small=None, sorter=None):
        random.shuffle(array)
        if adaptive:
            QuickSort.__adaptsort(array, 0, len(array)-1, small, sorter)
        else:
            QuickSort.__sort(array, 0, len(array)-1)

