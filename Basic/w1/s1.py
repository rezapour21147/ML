from logging import exception
import random


def make_rand(number):
    a = random.choice(number)
    number.remove(a)
    return a

def rand_list(list , n):
    global numbers
    l2 = []
    for i in range(n):
        l2.append(list[make_rand(numbers)])
    return sorted(l2)



list = eval(input())
n = int(input())
numbers = [i for i in range(len(list))]
if  len(list) % n == 0 :
    while len(numbers) != 0:
        ans = rand_list(list , n)
        print(ans)
else:
    raise BaseException('invalid number')
    