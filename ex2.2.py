import json

data = json.load(open('ex2.json'))
count = 0
counts = []
timings = []


for i in range(3):
    start = perf_counter()
    func1(data[i], 0, len(data[i]) - 1)
    end = perf_counter()
    counts.append(count)
    count += 1
    timings.append(end - start)


plt.plot(counts, timings)
plt.show()