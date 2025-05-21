import timeit
import matplotlib.pyplot as plt

def Input(Array, n):
    for i in range(n):
        ele = int(input("Arr : "))
        Array.append(ele)
def binary_search(Array, key):
    low = 0
    high = len(Array) - 1

    while low <= high:
        mid = (low + high) // 2
        if Array[mid] == key:
            return True
        elif Array[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return False

N = []
CPU = []

trail = int(input("Enter no. of trials: "))

for t in range(trail):
    Array = []
    print("\n-----> TRIAL NO :", t + 1)
    n = int(input("Enter number of elements: "))
    Input(Array, n)
    Array.sort()  
    print("Sorted Array:", Array)
    key = int(input("Enter key to search: "))
    start = timeit.default_timer()
    s = binary_search(Array, key)
    times = timeit.default_timer() - start

    print("Element Found =", s)
    N.append(n)
    CPU.append(round(times * 1000000, 2))

print("\nN\tCPU Time (µs)")
for t in range(trail):
    print(N[t], "\t", CPU[t])

plt.plot(N, CPU, label="Time vs Size")
plt.scatter(N, CPU, color="red", marker="*", s=50)
plt.xlabel('Array Size - N')
plt.ylabel('CPU Processing Time (µs)')
plt.title('Binary Search Time Efficiency')
plt.grid(True)
plt.legend()
plt.show()
