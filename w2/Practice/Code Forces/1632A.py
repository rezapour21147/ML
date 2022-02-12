def ABC(lenght , number):
    if lenght <= 2:
        if lenght==2 and number[1] == number[0]:
            return 'no'
        else:
            return 'yes'
    else:
        return 'no'

counter = int(input())
for i in range(counter):
    lenght = int(input())
    number = input()
    print(ABC(lenght , number))