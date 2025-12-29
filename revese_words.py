s="I am studying in aits"
res=""
word=""
for char in s:
    if char!=" ":
        word+=char
    else:
        res=word+""+res
        word=" "
res=word+""+res
print(res)