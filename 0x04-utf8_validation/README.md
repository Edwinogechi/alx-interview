
Project 0x04-utf8_validation
Overview
This project, titled 0x04-utf8_validation, focuses on implementing a program in C that validates if a given array of integers represents a valid UTF-8 encoding. UTF-8 is a variable-width character encoding capable of encoding all 1,112,064 valid character code points in Unicode using one to four one-byte (8-bit) code units.

The project aims to implement a function int utf8_validation(int *data, size_t len) that validates whether a given array data of integers represents a valid UTF-8 encoding. The function returns 1 if the array is a valid UTF-8 encoding, otherwise returns 0. The function also takes in the length of the array as the parameter len.

Project Files
utf8.h: Header file containing function prototype.
0-validate_utf8.c: Implementation file containing the utf8_validation function.
0-main.c: Main file containing the test cases to verify the functionality of utf8_validation function.
**0-utf8`: Executable file compiled from source files.
Compilation and Execution
To compile the project, execute the following command:

bash
Copy code
gcc -Wall -Werror -Wextra -pedantic 0-main.c 0-validate_utf8.c -o 0-utf8
To execute the program, run the compiled executable 0-utf8:

bash
Copy code
./0-utf8
Test Cases
The 0-main.c file contains test cases to verify the correctness of the utf8_validation function. These test cases cover various scenarios to ensure the function handles different inputs correctly.

How to Contribute
Contributions to this project are welcome. If you find any issues or improvements, feel free to open an issue or create a pull request in the project's repository.

License
This project is licensed under 


Tasks
0. UTF-8 Validation
mandatory
Write a method that determines if a given data set represents a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer
