x=[1,'liza',[4,5],'himani',8,7]
i=0
sum=0
while i<len(x):
    if type(x[i])==list:
        j=0
        # while j<len(x[i]):
        #     sum+=(x[i][j])
        #     j+=1
    elif type(x[i])==int:
        sum+=x[i]
    i+=1
print(sum)
