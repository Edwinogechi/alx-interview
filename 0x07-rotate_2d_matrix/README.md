Project Title: 0x07 Rotate 2D Matrix

Description:
The 0x07 Rotate 2D Matrix project is aimed at implementing an algorithm to rotate a given 2D matrix (list of lists) by 90 degrees clockwise in-place. This rotation operation involves rearranging the elements of the matrix such that each row becomes a column in the rotated matrix.

Features:

Rotate 2D Matrix: Provides functionality to rotate a given 2D matrix by 90 degrees clockwise without using any extra space.
In-Place Rotation: Performs the rotation operation in-place, meaning that it modifies the original matrix without creating a new one.
Efficient Algorithm: Implements an efficient algorithm to achieve the rotation with a time complexity of O(N^2), where N is the size of the matrix.
Usage:

Input: Provide a 2D matrix (list of lists) as input, where each inner list represents a row of the matrix.
Output: Obtain the rotated matrix as the output, with each row of the original matrix becoming a column in the rotated matrix.
Example:

csharp
Copy code
Input:
[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

Output:
[
  [7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]
]
Installation:

This project does not require any installation steps. Simply import the provided function(s) for rotating the 2D matrix into your Python script and use them as needed.

Contributing:

Contributions to the project are welcome! If you'd like to contribute, please fork the repository, create a new branch for your changes, commit your changes, and create a pull request.

License:

This project is licensed under the [Specify License] License. See the LICENSE file for details.

Contact:

For any inquiries or support, please contact [Maintainer Name] at [contact@example.com].

Feel free to customize this README according to the specific details and requirements of your project!

Tasks
0. Rotate 2D Matrix
mandatory
Given an n x n 2D matrix, rotate it 90 degrees clockwise.

Prototype: def rotate_2d_matrix(matrix):
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.
