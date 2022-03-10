


def sort_counter(testlist):
    counter = 0 
    for i in range(len(testlist)-1):
        if testlist[i] > testlist[i+1] :
            counter += 1
    return counter

print(sort_counter([1,5,8,12,6,15,21,42,13]))

