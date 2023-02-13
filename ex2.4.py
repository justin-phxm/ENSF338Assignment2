import sys
import json
import matplotlib.pyplot as plt
from time import perf_counter
sys.setrecursionlimit(20000)

def func1(arr, low, high):
    while low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        low = pi + 1


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


for i in data:
    start = perf_counter()
    func1(i, 0, len(i) - 1)
    end = perf_counter()
    counts.append(count)
    count += 1
    timings.append(end - start)

plt.plot(counts, timings)
plt.title("Quick Sort")
plt.xlabel("Arrays")
plt.xticks(range(0,len(data)))
plt.ylabel("Time (s)")
plt.show()