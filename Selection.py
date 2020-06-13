
class Selection():
    @staticmethod
    def sort(array, low=0, high=None):
        if not high:
            high = len(array)-1
        for i in range(low, high+1):
            min = i
            for j in range(i+1, high+1):
                if array[j] < array[min]:
                    min = j
            array[min], array[i] = array[i], array[min]


