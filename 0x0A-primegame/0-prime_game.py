#!/usr/bin/python3
"""Module for Prime game """


def sieve_of_eratosthenes(max_n):
    """Generates a list where the index represents the number
        and the value at each index indicates whether it is prime"""
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes
    p = 2
    while p * p <= max_n:
        if primes[p]:
            for i in range(p * p, max_n + 1, p):
                primes[i] = False
        p += 1
    return primes


def count_prime_rounds(primes, n):
    """For each n, count how many primes are available.
        The winner of the round depends on the parity of
        this count (odd or even)"""
    round_winner = 0
    for i in range(2, n + 1):
        if primes[i]:
            round_winner += 1
    return round_winner % 2


def isWinner(x, nums):
    """Determine Round Winner"""
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
        else:
            if count_prime_rounds(primes, n) == 1:
                maria_wins += 1
            else:
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
