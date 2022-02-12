def determine(matrix):
    if len(matrix) == len(matrix[0]):
        if len(matrix) == 1:
            return matrix[0][0]
        elif len(matrix) == 2:
            return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
        else:
            pass
