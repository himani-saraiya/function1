def fun(a):
    print(a*n)
    if a==10:
        return 1
    return fun(a+1)-1
n=int(input("enter no.:"))
fun(1)
        