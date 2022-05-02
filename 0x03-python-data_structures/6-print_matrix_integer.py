#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in row:
            if i is not row[len(row) - 1]:
                print(i, end=' ')
            else:
                print(i, end='')
        print()
