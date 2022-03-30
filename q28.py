def solve(questionlist):
    print(questionlist)
    if len(questionlist)==1:
        return int(questionlist[0])
    elif len(questionlist)==3:
        return solve(int(questionlist[0]), questionlist[1], int(questionlist[2]))
    else:
        return solve(solve(questionlist[:-2]), questionlist[-2], int(questionlist[-1])) 
solve(['3', '+', '5', '-', '2', '*', '4', '/', '2', '+', '8', '-', '10', '*', '9', '/', '3'])