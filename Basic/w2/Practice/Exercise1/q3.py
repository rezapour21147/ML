def max(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max
    
def min(list):
    min = list[0]
    for i in list:
        if i < max:
            min = i
    return min

list = input().split()
number_list = [int(i) for i in list]
print('max is:' , max(number_list))
print('min is:' , min(number_list))