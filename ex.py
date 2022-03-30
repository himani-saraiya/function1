x=['puja','rani','behra']
y=['trupti','mayi','singh']
i=0
list=[]
while i<len(x):
    j=0
    while j<len(y):
        if i==j:
            list.append(x[i])
            list.append(y[j])
        j=j+1
    i=i+1
print(list)
