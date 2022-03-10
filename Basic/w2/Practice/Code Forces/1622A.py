def Construct_a_Rectangle(sticks):
    if sticks[0] == sticks[1] :
        if sticks[2] % 2 == 0:
            return 'yes'
        else:
            return 'no'
    elif sticks[0] == sticks[2] :
        if sticks[1] % 2 == 0:
            return 'yes'
        else:
            return 'no'
    elif sticks[2] == sticks[1] :
        if sticks[0] % 2 == 0:
            return 'yes'
        else:
            return 'no'
    else:
        ma = sticks.index(max(sticks))
        if ma == 0:
            if sticks[1] + sticks[2] == sticks[ma]:
                return 'yes'
            else:
                return 'no'
        elif ma == 1:
            if sticks[0] + sticks[2] == sticks[ma]:
                return 'yes'
            else:
                return 'no'
        elif ma == 2:
            if sticks[1] + sticks[0] == sticks[ma]:
                return 'yes'
            else:
                return 'no'


counter = int(input())
for i in range(counter):
    list = input().split()
    sticks = [int(j) for j in list]
    print(Construct_a_Rectangle(sticks))