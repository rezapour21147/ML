def rectangle(length , height):
    print(' '*(height-2) , '*'*length)
    n = height-3
    for i in range(height-2):
        print(' '*n , '*' , ' '*(length-4) , '*')
        n -= 1
    print('*'*length)

rectangle(5 , 4)