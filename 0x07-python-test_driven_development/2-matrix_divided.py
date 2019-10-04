#!/usr/bin/python3
def matrix_divided(matrix, div):
    diverr = "div must be a number"
    zererr = "division by zero"
    rowerr = "Each row of the matrix must have the same size"
    ma_err = "matrix must be a matrix (list of lists) of integers/floats"
    if (matrix == [[]] or matrix == []) or len(matrix) == 0:
        raise TypeError(ma_err)
    if not isinstance(matrix[0], list):
        raise TypeError(ma_err)
    if matrix:
        len_row = len(matrix[0])
    if not isinstance(div, (float, int)):
        raise TypeError(diverr)
    if div is 0:
        raise ZeroDivisionError(zererr)
    if isinstance(matrix, list):
        for row in matrix:
            if isinstance(row, list):
                for number in row:
                    if len(row) != len_row:
                        raise TypeError(rowerr)
                    if not isinstance(number, int) and \
                       not isinstance(number, float):
                        raise TypeError(ma_err)
            else:
                raise TypeError(ma_err)
    else:
        raise TypeError(ma_err)
    new_m = [x[:] for x in matrix]
    for row in new_m:
        for number in range(len(row)):
            row[number] /= div
            row[number] = round(row[number], 2)
    return new_m
