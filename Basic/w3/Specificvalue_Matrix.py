from Matrix_Determinant import determinant
from sympy import symbols , Eq , solve

def specific_value(matrix):
    y = symbols('y')
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j :
                matrix[i][j] -= y
    equation = Eq(determinant(matrix))
    return solve(equation , y)

print(specific_value([[2 , -1 , 1] , [0 , 3 , -1] , [2 , 1 , 3]]))