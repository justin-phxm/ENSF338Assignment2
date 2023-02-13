import json
import sys
from time import perf_counter
import matplotlib.pyplot as plt
sys.setrecursionlimit(20000)


def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)


def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high
    
data = json.load(open('ex2.json'))
count = 0
counts = []
timings = []


for i in range(len(data)):
    start = perf_counter()
    func1(data[i], 0, len(data[i]) - 1)
    end = perf_counter()
    counts.append(count)
    count += 1
    timings.append(end - start)

plt.plot(counts, timings)
plt.title("Quick Sort")
plt.xlabel("Arrays")
# plt.xticks(range(0,3))
plt.ylabel("Time (s)")
plt.show()