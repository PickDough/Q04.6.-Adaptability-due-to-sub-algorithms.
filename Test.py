import random
import time

from Insertion import Insertion
from Selection import Selection
from mergesort import Merge
from quicksort import QuickSort


class SingleTest():
    def __init__(self, sorter, array):
        self.sorter = sorter
        self.array = array

    def test(self):
        copy = self.array.copy()
        start = time.time()
        self.sorter.sort(copy)
        end = time.time()
        return end - start

class DoubleTest():
    def __init__(self, sorter1, sorter2, small, array):
        self.bigsort, self.smallsort = sorter1, sorter2
        self.array = array
        self.small = small

    def test(self):
        copy = self.array.copy()
        start = time.time()
        self.bigsort.sort(copy, True, self.small,  self.smallsort)
        end = time.time()
        return end - start

def createArray(n):
    return [random.randrange(1, n) for i in range(n)]

sorters = [Insertion, Selection, Merge, QuickSort]
sizes = [1_000, 10_000, 100_000, 1_000_000]

"Testing for Single Sorter"
# for n in sizes:
#     array = createArray(n)
#     for srt in sorters:
#         if (srt == Selection or srt == Insertion) and n >10_000:
#             continue
#         single = SingleTest(srt, array)
#         print("The",srt.__name__,"sorted",n,"elements in",single.test())
#
#     print("-"*100)
"Searching for threshold for QuickSort"  # 11
# quick_pairs = []
# for n in (1_000, 10_000, 100_000,):
#     array = createArray(n)
#     for srt in (Selection, Insertion):
#         min = 100
#         smoll = 0
#         t = 0
#         for s in range(6, 13):
#             double = DoubleTest(QuickSort, srt, s, array)
#             t = double.test()
#             print ("The time for size", n,"threshold", s, "and (QuickSort +", srt.__name__+")", "is", t)
#             if t < min:
#                 min = t
#                 smoll = s
#         quick_pairs.append(smoll)
#         print()
#         print("The fastest threshold for QuickSort +",srt.__name__,"is",smoll,"with size",n,"and time",min)
#         print("-"*100)
# print(quick_pairs)
# quick_average = sum(quick_pairs)//len(quick_pairs)
# print("The average threshold for QuickSort is", quick_average)

# array = createArray(10_000)
# print(QuickSort.sort(array.copy(),True, 9, Selection) == QuickSort.sort(array.copy(),True, 9, Insertion))

"Searching for Merge threshold"  # 9
# merge_pairs = []
# for n in (1_000, 10_000, 100_000,):
#     array = createArray(n)
#     for srt in (Selection, Insertion):
#         min = 100
#         smoll = 0
#         t = 0
#         for s in range(6, 13):
#             double = DoubleTest(Merge, srt, s, array)
#             t = double.test()
#             print ("The time for size", n,"threshold", s, "and (Merge +", srt.__name__+")", "is", t)
#             if t < min:
#                 min = t
#                 smoll = s
#         merge_pairs.append(smoll)
#         print()
#         print("The fastest threshold for Merge +",srt.__name__,"is",smoll,"with size",n,"and time",min)
#         print("-"*100)
# print(merge_pairs)
# merge_average = sum(merge_pairs)//len(merge_pairs)
# print("The average threshold for Merge is", merge_average)

"Comparing adaptive and non-adaptive approach"
quick_threshold = 11 #quick_average
merge_threshold = 9 #merge_average
for big in (QuickSort, Merge):
    for n in sizes:
        array = createArray(n)
        single = SingleTest(big, array)
        single_time = single.test()
        for srt in (Selection, Insertion):
            if big == QuickSort:
                smoll = quick_threshold
            else:
                smoll = merge_threshold
            double = DoubleTest(big, srt, smoll, array)
            double_time = double.test()
            print("Time for",big.__name__,"is",str(single_time)+", time for ("+big.__name__+" + "+srt.__name__+") is", double_time,"for size", n
                  , "\nwhich leads to", double_time-single_time, "time difference")
        print ("-" * 150)
    print ("-" * 150)

