import timeit
import matplotlib.pyplot as plt

fibUnoptimized = '''
def fib(n):
    if n == 1 or n == 2:
        return 1
    elif n > 0:
        return fib(n-1) + fib(n-2)
'''
fibOptimized = '''
cache = {}
def fib2(n):
    if n == 0 or n == 1:
        return n
    else:
        if n in cache:
            return cache[n]
        else:
            cache[n] = fib2(n-1) + fib2(n-2)
            return cache[n]
'''

timeFib = []
timeFib2 = []
for i in range(35): 
    timeFib.append(timeit.timeit(stmt= f'fib({i})', setup= fibUnoptimized, number= 1))
    timeFib2.append(timeit.timeit(stmt= f"fib2({i})", setup= fibOptimized, number= 1))

plt.plot(timeFib, label= 'Unoptimized')
plt.plot(timeFib2, label= 'Optimized')
plt.title('Recursive Fibonacci(n)')
plt.xlabel('n times')
plt.ylabel('Time in seconds')
plt.legend()
plt.show()
