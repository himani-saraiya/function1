def fib(number):
    print(number)
    if number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fib(number-1) + fib(number-2)
fib(5)
