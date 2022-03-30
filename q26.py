def operate(num1, operator, num2):
    num=num1+num2
    print(num)
    if operator=='+':
        return num1 + num2
    elif operator=='-':
        return num1 - num2
    elif operator=='*':
        return num1 * num2
    else:
        return num1 / num2
operate(2,"+",3)