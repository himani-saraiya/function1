def even(a,b):
    i=0
    j=0
    while i<len(a):
        if a[i]%2==0 and b[i]%2==0:
            print("dono even hai")
        else:
            print("dono even nhi hai")
        i=i+1
        j=j+1
even([1,2,7,4],[5,4,3,9])