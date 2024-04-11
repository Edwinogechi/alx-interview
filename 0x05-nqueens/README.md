# 0x05-nqueens

## Description

This project implements a solution for the N-Queens problem using a backtracking algorithm in Python. The N-Queens problem is a classic problem in combinatorial optimization and computer science, where the task is to place N chess queens on an N×N chessboard so that no two queens threaten each other. In other words, no two queens share the same row, column, or diagonal.

## Features

- Solves the N-Queens problem for any given board size.
- Implements an efficient backtracking algorithm to find solutions.
- Provides a clear and understandable implementation in Python.

## Requirements

- Python 3.x
- bcrypt library (for password hashing, if used)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/0x05-nqueens.git

pip install bcrypt

Usage
Navigate to the project directory:

bash
Copy code
cd 0x05-nqueens
Run the nqueens.py file:

bash
Copy code
python nqueens.py
Follow the on-screen instructions to input the desired board size and view solutions.

Contributors
Your Name
License
This project is licensed under the MIT License - see the LICENSE file for details.

kotlin
Copy code

Feel free to adjust or expand this README as needed for your project!

Tasks
0. N queens
mandatory

Chess grandmaster Judit Polgár, the strongest female chess player of all time


The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

Usage: nqueens N
If the user called the program with the wrong number of arguments, print Usage: nqueens N, followed by a new line, and exit with the status 1
where N must be an integer greater or equal to 4
If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1
If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1
The program should print every possible solution to the problem
One solution per line
Format: see example
You don’t have to print the solutions in a specific order
You are only allowed to import the sys module
Read: Queen, Backtracking
