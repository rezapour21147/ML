def Integer_Diversity(numbers):
    odds = []
    equals = []
    negative = []
    for i in numbers:
        if i not in odds and i >= 0 and -i not in equals:
            odds.append(i)
        elif i < 0 and i not in negative and -i not in equals:
            negative.append(i)
        elif (i in odds and -i in negative) or (i in negative and -i in odds):
            pass
        elif i not in equals and -i not in equals and i != 0:
            equals.append(i)
    answer = len(odds) + len(equals) + len(negative)
    return answer

counter = int(input())
for i in range(counter):
    a = input()
    list = input().split()
    numbers = [int(j) for j in list]
    print(Integer_Diversity(numbers))