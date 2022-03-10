def Monitory(number):
    number = list(number)
    n1 = 0
    n0 = 0
    for j in number:
        if j == '0':
            n0 += 1
        elif j == '1':
            n1 += 1
    if n0 > n1:
        return n1
    elif n0 < n1:
        return n0
    elif n0 == n1:
        if len(number) == 2:
            return 0
        else:
            return n0-1


counter = int(input())
for i in range(counter):
    number = input()
    print(Monitory(number))

