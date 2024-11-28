def get_matrix(n, m, value):
    if n <= 0 or m <= 0:
        return []
    matrix = []
    for a in range(n):
        row = []
        for a in range(m):
            row.append(value)
        matrix.append(row)
    return matrix

one = get_matrix(1, 2, 4)
two = get_matrix(7, 5, 10)
three = get_matrix(0, 2, 9)

print(one)
print(two)
print(three)