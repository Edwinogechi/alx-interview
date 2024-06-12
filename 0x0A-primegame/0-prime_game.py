#!/usr/bin/python3
"""Determines the winner of the prime game"""

def isWinner(x, nums):
    """Function to determine the winner of the prime game"""
    if x < 1 or not nums:
        return None

    m_wins = 0
    b_wins = 0

    # Generate a prime numbers list based on the max no in nums
    n = max(nums)
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i**2, n + 1, i):
                primes[j] = False

    # Count the number of primes less than or equal to n in nums
    for num in nums:
        count = sum(primes[2:num+1])
        b_wins += count % 2 == 0
        m_wins += count % 2 == 1

    # Determine the winner
    if m_wins == b_wins:
        return None

    return 'Maria' if m_wins > b_wins else 'Ben'
