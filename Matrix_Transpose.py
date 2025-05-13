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

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transpose = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        transpose.append(row)
    return transpose

def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = input_matrix(rows, cols)

    transposed = transpose_matrix(matrix)

    print("\nOriginal Matrix:")
    for row in matrix:
        print(row)

    print("\nTransposed Matrix:")
    for row in transposed:
        print(row)

if __name__ == "__main__":
    main()
