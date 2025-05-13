def input_matrix(rows, cols):
    matrix = []
    print(f"Enter elements row by row ({rows}x{cols} matrix):")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Enter element [{i+1}][{j+1}]: "))
            row.append(element)
        matrix.append(row)
    return matrix

def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("\nEnter details for Matrix 1:")
    matrix1 = input_matrix(rows, cols)

    print("\nEnter details for Matrix 2:")
    matrix2 = input_matrix(rows, cols)

    result = add_matrices(matrix1, matrix2)

    print("\nResultant Matrix after Addition:")
    for row in result:
        print(row)

if __name__ == "__main__":
    main()
