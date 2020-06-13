import random


class Insertion():
    @staticmethod
    def sort(array, low=0, high=None):
        if not high:
            high = len(array)-1
        for i in range(low, high+1):
            for j in range(i, low, -1):
                if array[j] < array[j-1]:
                    array[j], array[j-1] = array[j-1], array[j]
                else:
                    break
