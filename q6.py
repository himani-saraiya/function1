def upper(case):
    i=0
    upper=0
    lower=0
    while i<len(case):
        if case[i]>="A" and case[i]<="Z":
            upper=upper+1
        if case[i]>="a" and case[i]<="z":
            lower=lower+1
        i=i+1
    print(upper)
    print(lower)
upper("The quick Brow Fox")