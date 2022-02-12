
def zip(*args):
    answer = []
    lens = [len(i) for i in args]
    counter = min(lens)
    for i in range(counter):
        list = []
        for j in args:
            list.append(j[i])
        answer.append(tuple(list))
    return answer