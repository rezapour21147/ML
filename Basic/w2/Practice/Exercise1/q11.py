import random

def guess_game():
    number = random.randint(1 , 20)
    for i in range(5):
        guess = int(input())
        if guess == number:
            print('You Win')
            return True
        else:
            print('Try Again')
    print('Game Over')
    print(f'The right number was {number}')

