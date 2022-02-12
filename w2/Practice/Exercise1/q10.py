massage = 'Babak Khorramdian'
print(massage[0])
print(massage[6])
massage_list= massage.split()
for i in massage_list:
    print(i)
print(massage[:12:2])
for i in massage:
    if i == 'm':
        print(True)
        break