#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor, rounded to 2 decimal places.

    Args:
        matrix (list of lists): The matrix containing intergers or floats.
        div: (int or float): The number to divide the elements by.

    Returns:
    lists of lists: A new matrix containing the results of the division

    Raises:
        TypeError: If matrix is not a list of lists of int/float,
                    if rows are not the same, or if div is not a number
        ZerodDivisionError: if div is == 0

    """

    # Validate 'div' type and value
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Validate 'matrix' structure (list of lists) and Non-emptiness
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be amatrix (list of lists) of intergers/floats")

    if not matrix or not matrix:
        # Handle cases where the matrix might be empty or a list of empty lists
        # Assuming non-empty rows are expected if matrix exists
        pass

    # Check for consistent row sizes and elements types
    if not matrix:
        return []

    first_row_len = len(matrix)

    for row in matrix:
        # validate row size
        if len(row) != first_row_len:
            raise TypeError("Each row of the matrix must have the same size")

        # Validate element type
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of intergers/floats")

    # Perform division and rounding, creating a new matrix
    new_matrix = []
    for row in matrix:
        new_row = [round(element/div, 2) for element in row]
        new_matrix.append(new_row)