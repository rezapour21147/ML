from typing import Optional


def  matrix_multiply(matrix1 , matrix2) -> Optional[list]:
    if len(matrix2) == len(matrix1[0]):
        new_matrix = [[0 for i in range(len(matrix1))] for j in range(len(matrix2[0]))]
        for i in matrix1:
            for n in range(len(matrix2[0])):
                for element in range(len(i)):
                    new_matrix[matrix1.index(i)][n] += i[element] * matrix2[element][n]
        return new_matrix
    else:
        raise BaseException('the column of first matrix must be equal to the row of second matrixs')

matrix1 = [[1, 3] , [2 , 4 ]]
matrix2 = [[3 , 4] ,[3 , 6 ]]
print(matrix_multiply(matrix1 , matrix2))


