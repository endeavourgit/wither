import timeit
import matplotlib.pyplot as plt
def Input(Array, n):
 for i in range(0, n):
    ele = int(input("Arr : "))
    Array.append(ele)

      
def linear_search(Array, key):
 for x in Array:
   if x == key:
       return True
 return False


N = []
CPU = []
trail = int(input("Enter no. of trails : "))


for t in range(0, trail):
    Array = []
    print("-----> TRAIL NO : ", t + 1)
    n = int(input("Enter number of elements : "))
    Input(Array, n)
    print(Array)
    key = int(input("Enter key :"))
    start = timeit.default_timer()
    s = linear_search(Array, key)
    print("Element Found = ", s)
    times = timeit.default_timer() - start
    N.append(n)
    CPU.append(round(float(times) * 1000000, 2))
    print("N CPU")

    
for t in range(0, trail):
    print(N[t], CPU[t])
plt.plot(N, CPU)
plt.scatter(N, CPU, color= "red", marker= "*", s=50)
plt.xlabel('Array Size - N')
plt.ylabel('CPU Processing Time')
plt.title('Linear Search Time efficiency')
plt.show()
