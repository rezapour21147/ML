def kind_int(number):
    if number % 2==0:
        return 'even'
    else:
        return 'odd'

number = int(input())
print(kind_int(number))