def determinant(matrix):
    answer = 0
    if len(matrix) == len(matrix[0]):
        if len(matrix) == 1:
            return matrix[0][0]
        elif len(matrix) == 2:
            return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
        else:
            for i in range(len(matrix)):
                operation_matrix = matrix.copy()
                operation_matrix.pop(0)
                for j in range(len(operation_matrix)):
                    operation_matrix[j] = operation_matrix[j][0:i] + operation_matrix[j][i+1:]
                sign = (-1) ** (i % 2)
                sub_det = determinant(operation_matrix)
                answer += sign * matrix[0][i] *sub_det
            return answer

