def fruits(fruit_list):
    answer = {}
    for i in fruit_list:
        if i['shape'] == 'sphere' and 300 <= i['mass'] <= 600 and 100 <= i['volume'] <= 500:
            if i['name'] in answer.keys():
                answer[i['name']] += 1
            else:
                answer[i['name']] = 1
    return answer
