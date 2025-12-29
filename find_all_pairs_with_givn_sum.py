s=[1,4,6,0,2,9,5]
res=6
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i]+s[j]==res:
            print([s[i],s[j]])