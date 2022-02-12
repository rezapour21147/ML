def game(number):
    n1 = number % 10
    n2 = (number - n1) / 10
    return int(abs(n2 - n1))


