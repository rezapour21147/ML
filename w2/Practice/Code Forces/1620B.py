def Triangles_On_Rectangle(cordinates , horizental1 , horizental2 , vertical1 , vertical2):
    if horizental1[-1]-horizental1[0] >= horizental2[-1]-horizental2[0]:
        h = (horizental1[-1]-horizental1[0]) * cordinates[1]
    else:
        h = (horizental2[-1]-horizental2[0]) * cordinates[1]
    if vertical1[-1]-vertical1[0] >= vertical2[-1]-vertical2[0]:
        w = (vertical1[-1]-vertical1[0]) * cordinates[0]
    else:
        w = (vertical2[-1]-vertical2[0]) * cordinates[0]
    if h >= w:
        return h
    else:
        return w

Counter = int(input())
for i in range(Counter):
    cordinates=[int(j) for j in input().split()]
    horizental1 = [int(j) for j in input().split()]
    horizental2 = [int(j) for j in input().split()]
    vertical1 = [int(j) for j in input().split()]
    vertical2 = [int(j) for j in input().split()]
    horizental1.pop(0)
    horizental2.pop(0)
    vertical1.pop(0)
    vertical2.pop(0)
    print(Triangles_On_Rectangle(cordinates , horizental1 , horizental2  ,vertical1 , vertical2))
    