s="studying"
res=""
for char in s:
    if char not in "aeiouAEIOU":
        res+=char
print(res)