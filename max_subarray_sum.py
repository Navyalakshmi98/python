s=[3,6,11,-1,-9,50]
res=float('-inf')
count=0
for num in s:
    count=count+num
    if count>res:
        res=count
    if count<0:
        count=0
print(res)