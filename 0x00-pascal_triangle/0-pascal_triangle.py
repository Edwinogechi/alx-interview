#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    Defines a function that returns a lists of integers
    representing the Pascal’s triangle
    """

    # Check if n is less than or equal to 0 and return an empty list
    if n <= 0:
        return []

    # Initialize the Pascal's triangle with the first row
    triangle = [[1]]

    # Loop to generate subsequent rows of the triangle
    while len(triangle) != n:

        # Get the previous row of the triangle
        previous = triangle[-1]

        # Initialize the current row with the first element
        current = [1]

        # Calculate each element of the current row
        for i in range(len(previous) - 1):

            # Add the sum of adjacent elements from the previous row
            current.append(previous[i] + previous[i + 1])

        # Add the last element of the current row
        current.append(1)

        # Add the current row to the triangle
        triangle.append(current)

    # Return the Pascal's triangle
    return triangle
