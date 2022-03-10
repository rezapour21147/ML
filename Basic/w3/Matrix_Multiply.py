from functools import reduce

def multiply(mat1 , mat2):
    answer=[]
    mat2_column = list(map(list , list(zip(*mat2))))
    if len(mat2) == len(mat1[0]):
        for i in range(len(mat1)):
            new_row =[]
            for j in range(len(mat2_column)):
                new_row.append(reduce(lambda a , b:a+b , map( lambda a, b: a * b , mat1[i] , mat2_column[j])))
            answer.append(new_row.copy())
        return answer
    else:
        raise Exception

