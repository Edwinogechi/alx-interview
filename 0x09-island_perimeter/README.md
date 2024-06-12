0x09-island_perimeter
Description
This project is aimed at solving the problem of calculating the perimeter of an island represented by a grid. Given a 2D grid map of 1s (land) and 0s (water), this script calculates the perimeter of the island formed by the land cells.

Table of Contents
Description
Installation
Usage
Contributing
License
Installation
To install the project, follow these steps:

Clone the repository:
bash
Copy code
git clone https://github.com/your_username/0x09-island_perimeter.git
Navigate to the project directory:
bash
Copy code
cd 0x09-island_perimeter
Usage
To use the script, follow these instructions:

Import the island_perimeter function from the island_perimeter.py module.
Call the island_perimeter function with a 2D grid map of 1s and 0s as input.
The function returns the perimeter of the island formed by the land cells.
Example:

python
Copy code
from island_perimeter import island_perimeter

grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

perimeter = island_perimeter(grid)
print("Perimeter of the island:", perimeter)
Contributing
Contributions are welcome! To contribute to this project, follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/improvement).
Make your changes.
Commit your changes (git commit -am 'Add some feature').
Push to the branch (git push origin feature/improvement).
Create a new Pull Request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Tasks
0. Island Perimeter
mandatory
Create a function def island_perimeter(grid): that returns the perimeter of the island described in grid:

grid is a list of list of integers:
0 represents water
1 represents land
Each cell is square, with a side length of 1
Cells are connected horizontally/vertically (not diagonally).
grid is rectangular, with its width and height not exceeding 100
The grid is completely surrounded by water
There is only one island (or nothing).
The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).
