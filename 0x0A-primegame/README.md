0x0A-primegame
Description
This project focuses on implementing a game algorithm for finding prime numbers efficiently. Given a list of integers, the script determines the winner of a prime game between two players. The players take turns selecting prime numbers from the list, and the player with no prime numbers left to choose loses the game.

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
git clone https://github.com/your_username/0x0A-primegame.git
Navigate to the project directory:
bash
Copy code
cd 0x0A-primegame
Usage
To use the script, follow these instructions:

Import the isWinner function from the 0-primegame.py module.
Call the isWinner function with a list of integers as input.
The function returns the name of the player who wins the prime game.
Example:

python
Copy code
from 0-primegame import isWinner

piles = [3, 4, 6, 8]
winner = isWinner(4, piles)
print("Winner of the prime game:", winner)
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
0. Prime Game
mandatory
Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including n, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.

Prototype: def isWinner(x, nums)
where x is the number of rounds and nums is an array of n
Return: name of the player that won the most rounds
If the winner cannot be determined, return None
You can assume n and x will not be larger than 10000
You cannot import any packages in this task
Example:

x = 3, nums = [4, 5, 1]
First round: 4

Maria picks 2 and removes 2, 4, leaving 1, 3
Ben picks 3 and removes 3, leaving 1
Ben wins because there are no prime numbers left for Maria to choose
Second round: 5

Maria picks 2 and removes 2, 4, leaving 1, 3, 5
Ben picks 3 and removes 3, leaving 1, 5
Maria picks 5 and removes 5, leaving 1
Maria wins because there are no prime numbers left for Ben to choose
Third round: 1

Ben wins because there are no prime numbers for Maria to choose
Result: Ben has the most wins
