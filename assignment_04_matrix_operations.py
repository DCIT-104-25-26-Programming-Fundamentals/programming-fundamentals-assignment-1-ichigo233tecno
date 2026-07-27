def read_matrix(rows, cols, label=""):
    """Read an rows x cols matrix from the user, one row per line."""
    matrix = []
    for i in range(rows):
        while True:
            row_input = input(f"Enter row {i + 1}{' of ' + label if label else ''}: ")
            row_values = row_input.split()
            if len(row_values) != cols:
                print(f"Error: expected {cols} values, got {len(row_values)}. Try again.")
                continue
            matrix.append([int(val) for val in row_values])
            break
    return matrix


def print_matrix(matrix, title=""):
    """Display a matrix in a neat, aligned grid."""
    if title:
        print(f"\n{title}")

    # Find the widest number so columns line up neatly
    width = max(len(str(val)) for row in matrix for val in row)

    for row in matrix:
        print("  ".join(str(val).rjust(width) for val in row))


def transpose_matrix(matrix):
    """Return the transpose of a matrix (rows become columns)."""
    rows = len(matrix)
    cols = len(matrix[0])

    # Build an empty cols x rows result matrix
    result = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


def add_matrices(matrix_a, matrix_b):
    """Return the element-wise sum of two same-sized matrices."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]

    return result


def multiply_matrices(matrix_a, matrix_b):
    """Return the matrix product A x B, where A is MxN and B is NxP."""
    m = len(matrix_a)        # rows of A
    n = len(matrix_a[0])     # cols of A / rows of B
    p = len(matrix_b[0])     # cols of B

    result = [[0 for _ in range(p)] for _ in range(m)]

    for i in range(m):
        for j in range(p):
            total = 0
            for k in range(n):
                total += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = total

    return result


if __name__ == "__main__":

    # -------------------------------------------------------------------
    # PART A — Transpose
    # -------------------------------------------------------------------
    print("=== PART A: Transpose a Matrix ===")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix(rows, cols)

    print_matrix(matrix, "Original Matrix:")
    transposed = transpose_matrix(matrix)
    print_matrix(transposed, "Transposed Matrix:")

    # -------------------------------------------------------------------
    # PART B — Addition
    # -------------------------------------------------------------------
    print("\n=== PART B: Add Two Matrices ===")
    add_rows = int(input("Enter number of rows for both matrices: "))
    add_cols = int(input("Enter number of columns for both matrices: "))

    print("Matrix A:")
    matrix_a = read_matrix(add_rows, add_cols, "Matrix A")
    print("Matrix B:")
    matrix_b = read_matrix(add_rows, add_cols, "Matrix B")

    sum_result = add_matrices(matrix_a, matrix_b)
    print_matrix(matrix_a, "Matrix A:")
    print_matrix(matrix_b, "Matrix B:")
    print_matrix(sum_result, "Sum (A + B):")

    # -------------------------------------------------------------------
    # PART C — Multiplication
    # -------------------------------------------------------------------
    print("\n=== PART C: Multiply Two Matrices ===")
    m = int(input("Enter rows of Matrix A: "))
    n = int(input("Enter columns of Matrix A (= rows of Matrix B): "))
    p = int(input("Enter columns of Matrix B: "))

    print("Matrix A:")
    mat_a = read_matrix(m, n, "Matrix A")
    print("Matrix B:")
    mat_b = read_matrix(n, p, "Matrix B")

    product = multiply_matrices(mat_a, mat_b)
    print_matrix(mat_a, "Matrix A:")
    print_matrix(mat_b, "Matrix B:")
    print_matrix(product, "Product (A x B):")