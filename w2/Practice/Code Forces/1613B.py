def Absent_Reminder(n , numbers):
    count = int(n/2)
    m = 0
    numbers.sort(reverse = True)
    for i in range(len(numbers)):
        for j in range(i+1 , len(numbers)):
            if numbers[i] != numbers[j] and numbers[i] % numbers[j] not in numbers:
                print(f'{numbers[i]} {numbers[j]}')
                m += 1
                if m == count:
                    return True

counter = int(input())
for i in range(counter):
    n = int(input())
    numbers = [int(j) for j in input().split()]
    Absent_Reminder(n , numbers)
