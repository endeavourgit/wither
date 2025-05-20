import timeit

def polynomial_BF(poly, x, n):
    
    result = 0
    
    for i in range(n):
        
        Sum = poly[i]
        
        for j in range(n - i - 1):
            Sum = Sum * x
        
        result = result + Sum
    
    print("Value of polynomial 2x^3 - 6x^2 + 2x - 1 for x = 3 using [BRUTE FORCE method]:", result)

def horner(poly, x, n):
    
    res = poly[0]
    
    for i in range(1, n):
        res = res * x + poly[i]
    print("Value of polynomial 2x^3 - 6x^2 + 2x - 1 for x = 3 using [HORNER method]:", res)



poly = [2, -6, 2, -1]
x = 3
n = len(poly)

start1 = timeit.default_timer()
polynomial_BF(poly, x, n)
t1 = timeit.default_timer() - start1

start2 = timeit.default_timer()
horner(poly, x, n)
t2 = timeit.default_timer() - start2

print("Time complexity of Brute Force method O(n^2):", t1)
print("Time complexity of Horner method O(n):", t2)
