def Make_AP(list):
    if list[2] - list[1] == list[1] - list[0]:
        return 'yes'
    else:
        d = (list[2] - list[0])/2
        if (list[2] - d) % list[1] == 0 and (list[2] - d) >= list[1]:
            return 'yes'
        d = list[2] - list[1]
        if (list[1] - d) % list[0] == 0 and (list[1] -d) >= list[0]:
            return 'yes'
        d = list[1] - list[0]
        if (list[1] + d) % list[2] == 0 and (list[1] + d) >= list[2]:
            return 'yes'
        return 'no'

counter = int(input())
for i in range(counter):
    list = input().split()
    list1 = [int(j) for j in list]
    print(Make_AP(list1))