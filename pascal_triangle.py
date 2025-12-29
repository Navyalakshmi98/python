import math
def helper(n,r):
    res=math.factorial(n-1)//(math.factorial(n-r)*math.factorial(r-1))
    print(res,end=" ")
for i in range(1,10):
    for j in range(1,i+1):
        helper(i,j)
    print()