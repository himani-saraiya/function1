def cal(weight,height):
    bmi=weight/height
    if bmi<=18.5:
        print("underweight")
    if bmi<=225.0:
        print("normal")
    if bmi<=30.0:
        print("overweight")
    if bmi<=30:
        print("obese")
    else:
        print("not")
    weight=int(input("enter weight"))       
    height=int(input("enter height"))
cal(25,5)