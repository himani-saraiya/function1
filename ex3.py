x=[1,2,[3,4,5],5,6,[7,8,9]]
i=0
l=[]
sum=0
while i<len(x):
    if type(x[i])==list:
        # l.append(x[i])
        # print(l)
        print(x[i])
    i+=1