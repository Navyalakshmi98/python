s=[2,3,4,5,6,7,7,1]
freq={}
for num in s:
    if num in freq:
        freq[num]=freq[num]+1
    else:
        freq[num]=1
def majority_element(s):
    for num in s:
        if freq[num]>(num//2):
            return num
    return -1
print(majority_element(s))