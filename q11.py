def age():
    age=int(input("enter age"))
    if age>=18:
        print("teen drinks coke")
    elif age==21:
        print("yong adults drink beer")
    elif age>21:
        print("adult drink whisky")
    else:
        print("nothing")
age()