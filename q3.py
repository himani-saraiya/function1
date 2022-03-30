str=["delhi","delhi","mumbai","mumbai","delhi","chennai""chennai"]
i=0
a=[]
while i<len(str):
    if str[i] not in a:
        a.append(str[i])
    i=i+1
print(a)