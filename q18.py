def fun(a):
    print(a)
    if a==1:
        return 1
    return fun(a-1)
fun(5)