def manual_incrementing_matrix(size):
    matrix = [[None for y in range(size)]for x in range(size)]
    counter = 0
    for idx, el in enumerate(matrix):
        for nested_idx, nested_el in enumerate(el):
            matrix[idx][nested_idx] = counter + nested_idx
        counter += 1
    return matrix

print(manual_incrementing_matrix(5))