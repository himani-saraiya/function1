def pattern(number):
    print(number+3)
    if number == 10:
        return 1
    else:
        return pattern(number+3) 
pattern(1)