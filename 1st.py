import timeit
import matplotlib.pyplot as plt

def Input(Array, n):
    for i in range(n):
        ele = int(input("Arr : "))
        Array.append(ele)

def linear_search(Array, key):
    for x in Array:
        if x == key:
            return True
    return False

N = []
CPU = []

trail = int(input("Enter number of trials: "))

for t in range(trail):
    Array = []
    print("\n-----> TRIAL NO :", t + 1)
    n = int(input("Enter number of elements: "))
    Input(Array, n)
    print("Array:", Array)
    key = int(input("Enter key to search: "))

    start = timeit.default_timer()
    found = linear_search(Array, key)
    end = timeit.default_timer()

    print("Element Found:", found)
    elapsed_time = (end - start) * 1_000_000  
    N.append(n)
    CPU.append(round(elapsed_time, 2))


print("\nN\tCPU Time (µs)")
for i in range(trail):
    print(N[i], "\t", CPU[i])


plt.plot(N, CPU, label='Time vs Size')
plt.scatter(N, CPU, color="red", marker="*", s=50)
plt.xlabel('Array Size - N')
plt.ylabel('CPU Time (µs)')
plt.title('Linear Search Time Efficiency')
plt.grid(True)
plt.legend()
plt.show()
