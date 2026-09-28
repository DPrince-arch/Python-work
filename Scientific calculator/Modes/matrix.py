def matrix_addition(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result

def matrix_subtraction(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions for subtraction.")

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)

    return result

def matrix_multiplication(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix for multiplication.")

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum_product = 0
            for k in range(len(matrix2)):
                sum_product += matrix1[i][k] * matrix2[k][j]
            row.append(sum_product)
        result.append(row)

    return result

def matrix_transpose(matrix):
    result = []
    for j in range(len(matrix[0])):
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        result.append(row)

    return result

def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Matrix must be square to calculate determinant.")

    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for c in range(len(matrix)):
            minor = [row[:c] + row[c+1:] for row in matrix[1:]]
            det += ((-1) ** c) * matrix[0][c] * determinant(minor)
        return det
    
def inverse(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Matrix must be square to calculate inverse.")

    det = determinant(matrix)
    if det == 0:
        raise ValueError("Matrix is singular and cannot be inverted.")

    if len(matrix) == 1:
        return [[1 / matrix[0][0]]]
    elif len(matrix) == 2:
        return [[matrix[1][1] / det, -matrix[0][1] / det],
                [-matrix[1][0] / det, matrix[0][0] / det]]
    else:
        cofactors = []
        for r in range(len(matrix)):
            cofactor_row = []
            for c in range(len(matrix)):
                minor = [row[:c] + row[c+1:] for row in (matrix[:r] + matrix[r+1:])]
                cofactor_row.append(((-1) ** (r + c)) * determinant(minor))
            cofactors.append(cofactor_row)
        cofactors_transposed = matrix_transpose(cofactors)
        inverse_matrix = [[cofactors_transposed[r][c] / det for c in range(len(cofactors_transposed))] for r in range(len(cofactors_transposed))]
        return inverse_matrix
    
