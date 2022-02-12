def transpose(matrix):
    new_matrix = [[0 for i in range(len(matrix))] for j in range(len(matrix[0])) if len(matrix) != 0]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix


