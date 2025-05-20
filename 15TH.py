from itertools import combinations

def Input(S, n):
  
    for i in range(n):
        ele = int(input("Arr : "))
        
        S.append(ele)

def sub_set_sum(size, S, d):
    count = 0
    for i in range(size + 1):
        for my_sub_set in combinations(S, i):
            if sum(my_sub_set) == d:
                print(list(my_sub_set))
                count += 1
    if count == 0:
        print("Subset Not found for the given d =", d)


S = []
n = int(input("Enter size: "))
Input(S, n)
print("Input array:", S)
d = int(input("Enter sum d: "))
print("The result is:")
sub_set_sum(n, S, d)
