def multiplication_table(size):
    # columns = size
    rows = [num + 1 for num in range(size)]
    columns = [num + 1 for num in range(size)]
    matrix = []

    for i in range(len(columns)):
        arr = []
        for j in range(len(rows)):
            arr.append(rows[i] * columns[j])
        matrix.append(arr)
    print(matrix)


    return matrix
