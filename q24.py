def getFibList(number):
    print(number)
    if number == 1:
        return [1]

    elif number == 2:
        return [1, 1]

    else:
        get_previous_fib_list = getFibList(number-1)
        new_last_element = get_previous_fib_list[-1] + get_previous_fib_list[-2]
getFibList(5)