def find(num1, num2, num3):
    list1 = [1 , 2 , 3 , 4]
    list2 = [num3 , num2 , num1]
    list3 = [i for i in list1 if  i not in list2]
    return list3[0]





