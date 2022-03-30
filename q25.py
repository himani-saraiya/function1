def ispresentinlist(numbertosearch, list_to_search):
    print(numbertosearch)
    counter = 0
    while (counter < len(list_to_search)):
        if number_to_search == list_to_search[counter]:
            return True
        counter += 1

    return False
ispresentinlist(5,[1,2,3,4,5,6])
